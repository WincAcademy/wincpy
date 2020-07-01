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
3. Write tests in `tests.py`
    1. Define a new function `test_example.py` **at the bottom** -- test order
       defines assignment number.
    2. Set the `filename` variable and init an empty list `result`
    3. Write tests as needed and collect tuples of `(requirement, passed_bool,
       error)` in `result` along the way.
4. Test your tests.
5. Commit and push.

### About writing tests

* Define tests in the order that the student would write their code. This way
  the student can test their code as they are writing it.
