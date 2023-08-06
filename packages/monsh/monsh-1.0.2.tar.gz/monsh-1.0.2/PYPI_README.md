# Monsh
Monsh is the python client script for [mon.sh](https://www.mon.sh), a service
which allows you to monitor and notify on long running shell commands from the web.

## Setup
To use the script effectively you would need to use an account on mon.sh, refer to the 
[quickstart guide](https://www.mon.sh/help/quickstart) for more information.

To configure the script initially with an API key, use `mon configure`.

## Usage
To use the script, simply pipe the command output of your script to the `mon`
command (or `monsh` if you prefer.)

```
python3 -c "import time; [print(i) or time.sleep(1) for i in range(20)]" |& mon
```

You can use `|` or `|&`, the latter also pipes the stderr output which is 
recommended. Note that the client works on multiple platforms but works best
on *nix type shells. While you can pipe output in powershell, the stderr
pipping does not work as easily.

### Options
* -w allows you to specify the workspace. A workspace is a virtual organization
structure for all jobs. If not specific everything falls into the default 
workspace. All event notification configuration happens at the workspace level.
* -k allows you to specify the API key for usage. If provided this overrides 
the API key in the config file that is setup via `mon configure`
* -l allows you to specify the log levels for the mon script itself. For example
you can use `mon -l DEBUG` to get additional information from the mon script.