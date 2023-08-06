#!/usr/bin/env python

# This file is the client side streaming agent that can be invoked via the
# command line e.g. `python3 do_something_complex.py | mon` which then
# starts a corresponding job on the server side and updates it with details
# as the command progresses.

# The client has to invoke, in an authorized manner (using an individual
# customers credentials), the job creation API. It should then receive some
# sort of endpoint or token or something to sync the logs to cloudwatch if
# that is the configuration. Every job is created in a "workspace", if no 
# workspace is specified the default workspace is used. Once the underling
# command that was streamed from terminates, the application should notify
# the server side by updating the job status. This should internally trigger
# notifications as configured on the workspace.

# A local mon.config can be used locally to specify the default workspace
# for a project and to overwrite settings or configure settings locally for
# notifications.

import uuid
import time
import sys
import json
import os
import logging
import io
import multiprocessing
from enum import Enum

import requests

## Config
API_ENDPOINT = "https://9ieavnhhuf.execute-api.us-east-1.amazonaws.com"
DEFAULT_WORKSPACE = "default"
MAX_BUFFER_TIME_SECONDS = 5
KEEP_ALIVE_INTERVAL = 10
MAX_BUFFER_TIME_LINES = 10000
CONFIG_FILE_API_KEY_KEY = "API_KEY"
API_KEY_ENV_NAME = "MON_API_KEY"
CONFIG_FILE_PATH = os.path.expanduser("~/.monsh")

class StdinProvider(Enum):
    AUTO = 0
    FOR_LINE = 1
    GETCH = 2
    READ_UNBUFFERED_BIT = 3

## This class provides lines to the logger from the input based on what's available
## on any given system. It prefers to use getch and then treats \r as new lines
## this helps pass progress bars to the backend.
class StdinLineProvider:
    def __init__(self, provider = StdinProvider.AUTO):
        self.provider = provider
        self.encoding = sys.stdin.encoding
        # if self.provider == StdinProvider.AUTO:
        #     import termios # we may need to do something specific for windows
        #     try:
        #         fd = sys.stdin.fileno()
        #         termios.tcgetattr(fd)
        #         self.provider = StdinProvider.GETCH
        #     except Exception as e:
        #         logging.debug(f"Failed to locate support for GETCH type provider. Received error {e}.")
        #         self.provider = StdinProvider.AUTO

        if self.provider == StdinProvider.AUTO:
            self.provider = StdinProvider.READ_UNBUFFERED_BIT

    def lines(self):
        if self.provider == StdinProvider.FOR_LINE:
            logging.debug("Using FOR_LINE provider to provide lines in generator.")
            for line in sys.stdin:
                yield line
        # elif self.provider == StdinProvider.GETCH:
        #     logging.debug("Using GETCH provider to provide lines in generator.")
        #     from getch import getch

        #     line_buffer = ""
        #     ch = getch()
        #     while ch:
        #         line_buffer += ch
        #         if ch == "\r" or ch == "\n":
        #             if line_buffer:
        #                 if not line_buffer == "\r":
        #                     yield line_buffer
        #             line_buffer = ""
        #         ch = getch()
        elif self.provider == StdinProvider.READ_UNBUFFERED_BIT:
            with io.open(sys.stdin.fileno(), 'rb', closefd=False, buffering=0) as stdin:
                line_buffer = b""
                ch_bit = stdin.read(1)
                while ch_bit:
                    line_buffer += ch_bit
                    if ch_bit == b"\r" or ch_bit == b"\n":
                        if line_buffer:
                            decoded_buffer = line_buffer.decode(self.encoding)
                            if not decoded_buffer == "\r":
                                yield decoded_buffer
                            line_buffer = b""
                    ch_bit = stdin.read(1)

# For authorization we need a JWT that our application should issue. Right now
# we don't have anything.
def get_api_token():
    api_token_env = os.getenv(API_KEY_ENV_NAME)
    if api_token_env:
        return api_token_env
    monsh_config_file_path = CONFIG_FILE_PATH
    if os.path.exists(monsh_config_file_path):
        with open(monsh_config_file_path, "r") as monsh_config_file:
            config_values = {}
            for line in monsh_config_file:
                line_pair = line.strip().split("=", 2)
                config_values[line_pair[0]] = line_pair[1]
            if CONFIG_FILE_API_KEY_KEY in config_values:
                return config_values[CONFIG_FILE_API_KEY_KEY]
    raise Exception(f"Could not find API KEY for mon.sh, run `mon configure` or set `{API_KEY_ENV_NAME}`")

# doing this for now instead of importing argparse but as this gets more 
# complicated we'll do it more fancy.
def get_arg(arg_list, *arg_names):
    if len(arg_list) < 1:
        return None
    normalized_arg_names = [arg_name.upper() for arg_name in arg_names]
    return_next = False
    for argument in arg_list:
        if return_next:
            return argument
        stripped_arg = argument.replace("-", "")
        if stripped_arg.upper() in normalized_arg_names:
            return_next = True
    return None

def keep_alive(api_key, job_identifier, verbosity):
    logging.basicConfig(level=logging._nameToLevel[verbosity])
    while True:
        response = requests.get(API_ENDPOINT + f"/jobs/keepalive?id={job_identifier}&apiKey={api_key}")
        if not response.ok or response.content == b"false":
            logging.warn(f"Failed to issue keep alive for job {job_identifier}")
        logging.debug(f"keep alive response: {response.content}")
        time.sleep(KEEP_ALIVE_INTERVAL)

def run():
    # We want to call the log endpoint whenever we have a large number of lines
    # to put OR we hit a certain amount of time (e.g. 1 second) and there is something
    # to be written. We can't exceed 5 TPS for log stream writes. But a log stream
    # is defined at the job level so it shouldn't be a problem as there should be
    # a single writer for a single job.

    if len(sys.argv) > 1 and (sys.argv[1].lower() == "configure" or sys.argv[1].lower() == "config"):
        print("Configuring mon...")
        api_key = input("Enter value for API Key:").strip()
        with open(CONFIG_FILE_PATH, "w") as monsh_config_file:
            monsh_config_file.write(f"{CONFIG_FILE_API_KEY_KEY}={api_key}")
        exit(0)

    api_token = get_arg(sys.argv, "k", "key", "apikey")
    if not api_token:
        api_token = get_api_token()
    job_identifier = str(uuid.uuid4())
    # time.time_ns() works in python3.7+
    job_start_time = time.time_ns() // 1_000_000

    workspace = get_arg(sys.argv, "w", "ws", "workspace")
    if not workspace:
        workspace = DEFAULT_WORKSPACE
    
    verbosity = get_arg(sys.argv, "v", "l", "verbosity", "loglevel", "level", "logs", "log")
    if not verbosity:
        verbosity = "INFO"
    logging.basicConfig(level=logging._nameToLevel[verbosity])
    logging.info(f"Starting mon job under workspace {workspace}: {job_start_time}/{job_identifier}")
    logging.info(f"->> https://www.mon.sh/job?id={workspace}%2F{job_start_time}%2F{job_identifier}")

    ## Create the job
    full_job_identifier = f"{workspace}/{job_start_time}/{job_identifier}"
    job_creation_response = requests.post(
        API_ENDPOINT + "/jobs", 
        headers={"Authorization": api_token },
        json={
            "operation": "create",
            "payload": {
                "Workspace_JobTime_JobIdentifier": full_job_identifier,
                "JobTime": job_start_time,
                "Status": "Running",
                "StatusDetail": {
                    "CompletionPercentage": "0%"
                }
            }
        })

    if not job_creation_response.ok:
        logging.warn(f"{job_creation_response.status_code}: {job_creation_response.content} during mon.sh job creation.")

    # Create the keep alive background process
    keep_alive_process = multiprocessing.Process(target=keep_alive, args=(api_token, full_job_identifier, verbosity), daemon=True)
    keep_alive_process.start()

    # Create the keep alive background process
    keep_alive_process = multiprocessing.Process(target=keep_alive, args=(api_token, full_job_identifier, verbosity), daemon=True)
    keep_alive_process.start()

    def flush_log_events(buffer, sequence_token = None):
        # print("Flushing log events...")
        result = requests.put(API_ENDPOINT + "/logs", 
            headers={"Authorization": api_token },
            json={
                "operation": "update",
                "payload": {
                    "Workspace_JobTime_JobIdentifier": f"{workspace}/{job_start_time}/{job_identifier}",
                    "SequenceToken": sequence_token,
                    "LogEvents": buffer
                }
            })
        
        if result.ok:
            return json.loads(result.content)["nextSequenceToken"]
        return sequence_token # return last sequence token

    last_write_time = time.time() # in seconds
    events_buffer = []
    sequence_token = None

    # TODO change this to a character based input so that we can capture progress
    # bars which rewrite the current line I think. These don't get captured.
    # TODO best effort with this and fallback if we can figure out if getch is not supported
    
    line_provider = StdinLineProvider()
    for line in line_provider.lines():
        sys.stdout.write(line)
        timestamp = time.time_ns() // 1_000_000
        events_buffer.append({"timestamp": timestamp, "message": line})
        if len(events_buffer) == MAX_BUFFER_TIME_LINES or time.time() - last_write_time > MAX_BUFFER_TIME_SECONDS:
            logging.debug(f"Mon flushing log buffer of size {len(events_buffer)}")
            if events_buffer:
                new_sequence_token = flush_log_events(events_buffer, sequence_token)
                if new_sequence_token == sequence_token:
                    logging.warn("Failed to write log events for mon.sh.")
                sequence_token = new_sequence_token
                events_buffer = []
            last_write_time = time.time()
    if events_buffer:
        flush_log_events(events_buffer, sequence_token)
        events_buffer = []

    ## Update the job
    completion_time = time.time_ns() // 1_000_000
    time.sleep(5) # delay artificially just to see if logs will process
    job_end_update_response = requests.put(API_ENDPOINT + "/jobs", 
        headers={"Authorization": api_token },
        json={
            "operation": "update",
            "payload": {
                "Workspace_JobTime_JobIdentifier": f"{workspace}/{job_start_time}/{job_identifier}",
                "JobTime": job_start_time,
                "Status": "Completed",
                "StatusDetail": {
                    "CompletionPercentage": "100%",
                    "CompletionStatus": "Success",
                    "CompletionTimestamp": completion_time
                }
            }
    })
    
    if not job_end_update_response.ok:
        logging.warn(f"{job_end_update_response.status_code}: {job_end_update_response.content} during mon.sh job finalization.")

    keep_alive_process.terminate()
    keep_alive_process.join()

    keep_alive_process.terminate()
    keep_alive_process.join()

if __name__ == "__main__":
    run()