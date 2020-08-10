# Wincpy

This is a tool students use to check their own code. Note: this rool runs
student code.  Before running it on students' code yourself, inspect the file
for malicious effects.

## Installation

`pip install git+https://github.com/WincAcademy/wincpy.git`

## Usage

!Outdated! -> Todo for @stfwn

```bash
wincpy 042_example.py
```

## Workflow for new assignments

!Outdated! -> Todo for @stfwn

1. Write an assignment description.
2. Write a solution in `solutions/042_example.py`
3. Write tests in `tests.py`
    1. Define a new function `test_042_example.py`.
    2. Init an empty list `result`.
    3. Write tests as needed and collect tuples of
       `(requirement_str, passed_bool)` in `result` along the way.
4. Test your tests.

### About writing tests

* Define tests in the order that the student would write their code. This way
  the student can test their code as they are writing it.

## TODO

- [ ] Apply fix so that non-code files are also included with setuptools
  packaging. Currently non-`.py` files are ignored. This breaks any starts and
  solutions that contain such files. See: https://python-packaging.readthedocs.io/en/latest/non-code-files.html
