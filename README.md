# Wincpy

This is a tool students use to start exercises and check how they are doing on
them.

Note: this rool runs student code. If you're every running it on students' code
yourself, inspect the file for malicious effects.

## Installation

`pip install git+https://github.com/WincAcademy/wincpy@release --user --upgrade`

## Usage
```bash
$ wincpy --help
usage: wincpy [-h] {start,check} ...

The Winc Python tool.

positional arguments:
  {start,check}  What wincpy should do in this run.
    start        Start a new assignment.
    check        Check an existing assignment.

optional arguments:
  -h, --help     show this help message and exit

$ wincpy start --help

usage: wincpy start [-h] winc_id

positional arguments:
  winc_id     Winc ID of an assignment to start.

optional arguments:
  -h, --help  show this help message and exit

$ wincpy check --help
usage: wincpy check [-h] [path]

positional arguments:
  path        Path containing assignment to check.

optional arguments:
  -h, --help  show this help message and exit
```

## Develop

**Important:** students install from the release branch, and Wincpy updates
itself from this branch as well. Students may update their version of Wincpy at
any time. **Test your changes before you commit to the release branch.**

### Adding exercises

0. Write your exercise text.
1. Generate a new Winc ID with [wincid](https://github.com/WincAcademy/wincid).
   Save the generated id in your clipboard and push the updated `json` to
   GitHub.
2. Write your solution in this repository, in a new directory: `wincpy/solutions/<winc_id>/`.
    - In `main.py`, there must be two properties:
        - `__winc_id__`: a string containing the Winc ID that this solution
          belongs to.
        - `__human_name__`: a string containing the human name for this
          exercise.
    - You may find other solutions are packages with a `__init__.py` file, this
      is a deprecated format and support for it will be removed in the future.
3. Write your tests in this repository, in a new file: `wincpy/tests/<winc_id>.py`
    - Within `<winc_id>.py`, define a function `run()` that takes a module as its
    argument and returns a list of tuples: `[(requirement_string,
    bool_requirement_satisfied)]`. The requirement strings are printed back to
    the student with thumbs up/down in green/red depending on the bool that
    it's matched with.
    - Look at the other test files for examples on how to write tests for the
      student module.
    - There are a number of helper functions available in `wincpy/helpers.py`.
    - There is also a template you could use for quick start: `wincpy/tests/template.py`.
4. Optional: if you would like to provide a starting point for students so that
   they don't have to write lame boilerplate code, do so in a new directory:
   `wincpy/starts/<winc_id>`.
   - Make sure your `main.py` contains the properties `__winc_id__` and
     `__human_name__`, just like the solution.
5. Test your solution, test and (optional) start.
    1. Run `pip install .` in the top-level directory of this repository.
    2. Go to your solution dir and run `wincpy check`.
    3. (optional) Go to your start dir and run `wincpy check`.
6. If everything works as expected, commit and push the added files to the
   remote for this repository on GitHub.
