# Wincpy

## Usage

Example:

```bash
python winc.py 00_print.py
```

Soon:

```bash
wincpy 00_print.py
```

## Workflow for new assignments

1. Write an assignment description and enter it into TalentLMS.
2. Write a solution in `solutions/42_example.py`
3. Write tests in `solution_tests.py`
    1. Subclass `TestCase`
    2. Set the assignment `filename` as a class variable
    3. Write tests as needed, with helpful error messages
    4. Don't forget to make use of the helpers in `helpers.py`
4. Append the new `TestCase` to the `tests` list in `winc.py`
    - TODO: make this dynamic to improve everyone's sanity.
5. Commit and publish to PyPi.
    - TODO: put wincpy on PyPi at all.
    - TODO: CI this.

### Writing tests

About writing tests:

* Define tests in the order that the student would write their code. This way
  the student can test their code as they are writing it.
