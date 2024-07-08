# Wincpy 1.3.3

[![.github/workflows/check-solutions.yml](https://github.com/WincAcademy/wincpy/actions/workflows/check-solutions.yml/badge.svg?branch=master)](https://github.com/WincAcademy/wincpy/actions/workflows/check-solutions.yml)

This is a tool students use to start exercises and check how they are doing on
them.

Note: `wincpy check` runs the code under inspection. If you're every running it
on students' code yourself, inspect the file for malicious effects.

## Installation

### Using pip

```sh
python3 -m pip install --extra-index-url https://packages.wincacademy.nl wincpy --user
```

### Using git

```sh
python3 -m pip install git+https://github.com/WincAcademy/wincpy@release --user --upgrade
```


## Usage

- `wincpy start winc_id`

  Creates a new folder in the current working directory with the human name of
  the exercise (e.g. 'print', 'functions' or 'classes') that contains the files
  required to do the exercise. This mechanic allows us to provide data files or
  boilerplate that the student can work with during the exercise.

  Here `winc_id` should be replaced by an identifier that corresponds to a
  specific exercise. For students, the Winc ID can be found at the top of the
  exercise instruction page.

- `wincpy check [path]`

  Checks an exercise for correctness and provides feedback on whether various
  components of the exercise are implemented correctly.

  Here `[path]` is an optional path (relative or absolute) to the directory
  containing the implementation to be checked. If it is omitted, the current
  working directory is used.

- `wincpy solve [path]`

  Checks an exercise for correctness and creates a new folder containing Winc's
  own solution for the exercise for a student to review and learn from. This
  command does *not* provide feedback to the student about their
  implementation; correctness is only a requirement for obtaining the reference
  solution.

  Here `[path]` is an optional path (relative or absolute) to the directory
  containing the implementation to be checked and solved. If it is omitted, the
  current working directory is used.

- `wincpy update`

  Updates Wincpy to the version on the *release*-branch of this repository on
  GitHub. Requires a working installation of pip in `$PATH`.

- `wincpy version`

  Show which version of Wincpy is installed.

See also `wincpy --help`.

## Develop

**Important:** students install from the release branch, and Wincpy updates
itself from this branch as well. Students may update their version of Wincpy at
any time. **Test your changes before you commit to the release branch.** Also:
don't forget to bump the version when you merge into the release branch,
otherwise pip will not update the local installation.

### Adding exercises

0. Write your exercise text.
1. Generate a new Winc ID with [wincid](https://github.com/WincAcademy/wincid).
   Save the generated id in your clipboard and push the updated `json` to
   GitHub.
2. **Write your solution** in this repository, in a new directory:
   `wincpy/solutions/<winc_id>/`.
    - In `main.py`, there must be two properties:
        - `__winc_id__`: a string containing the Winc ID that this solution
          belongs to.
        - `__human_name__`: a string containing the human name for this
          exercise.
3. **Write your checks** in this repository, in a new file:
   `wincpy/checks/<winc_id>.py`
    - Within `<winc_id>.py`, write test functions with names that start with
      `check_` (e.g.: `check_add_numbers`), similar to Pytest's `test_`. These
      functions will be called with a student module as their first argument.
    - Write assertions with helpful tips as their error message.
    - Everything else (running checks, catching errors, printing stuff, etc.)
      is handled by Wincpy.
    - There are a number of utility functions available in `wincpy/checks/utils.py`.
    - Look at the other test files for examples on how to write checks.
4. Optional: **write a start**. If you would like to provide a starting point
   for students so that they don't have to write boilerplate code, do so in a
   new directory: `wincpy/starts/<winc_id>`.
   - Make sure your `main.py` contains the properties `__winc_id__` and
     `__human_name__`, just like the solution.
5. Test your solution, test and (optional) start.
    1. Run `pip install -e .` in the top-level directory of this repository.
       (the `-e` flag installs a symlink to the wincpy module instead of a copy
       so you only need to install once if you're iterating)
    2. Go to your solution dir and run `wincpy check`. Ensure the solution passes.
    3. (optional) Go to your start dir and run `wincpy check`. Ensure your
       checks fail with useful tips.
6. If everything works as expected, commit and push the added files to the
   master branch for this repository on GitHub. If you're feeling daring today,
   bump the version and merge into the release branch.

## Exit Codes

| Code | Meaning                                                          |
| ---- | ---------------------------------------------------------------- |
| 0    | OK and solution passed                                           |
| 1    | OK but solution didn't pass                                      |
| 2    | Unknown Winc ID provided in start command                        |
| 3    | Couldn't create directory (FileExistsError)                      |
| 4    | No check for the found Winc ID                                   |
| 5    | No solution for the found Winc ID                                |
| 6    | Couldn't load Winc ID database                                   |
| 50   | Executing student code failed                                    |
| 51   | Importing student module failed                                  |
| 52   | Imported (supposed) student module has no `__winc_id__` property |

## Deployment

Manually trigger the Deploy GitHub Action to upload a new build to
packages.wincacademy.nl.

The version from [setup.py](/setup.py) is used for the build.
