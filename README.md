# Wincpy

This is a tool students use to check their own code. Note: this rool runs
student code.  Before running it on students' code yourself, inspect the file
for malicious effects.

## Installation

`pip install git+https://github.com/WincAcademy/wincpy.git`

## Usage

```bash
wincpy 042_example.py
```

## Workflow for new assignments

1. Write an assignment description and enter it into TalentLMS.
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

- [ ] Write test for `62311a1767294e058dc13c953e8690a4` (casting)
- [ ] Translate some Dutch snippets still lying around.
- [ ] Change abspath to relative path in user-facing string 'Output from ..' 
- [ ] Be more flexible with student module path designation on `wincpy check`
    - [ ] Support `wincpy check .`
    - [ ] Support `wincpy check example/`
    - [ ] Support `wincpy check ./this/here/example/`
