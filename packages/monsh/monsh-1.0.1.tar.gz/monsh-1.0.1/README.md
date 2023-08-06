# Example Commands
* `python3 -u test/example_script.py | python3 onemon.py`
* `pip3 install -e .`
* From the test folder `python3 -u example_script.py | onemon`

# Building
bump minor ver
`python -m build`
Refer to https://realpython.com/pypi-publish-python-package/#get-to-know-python-packaging
Generate a hash with `sha256sum *.whl` (replace * with file name) and UPDATE QUICKSTART with URL
Upload to mon-dist bucket