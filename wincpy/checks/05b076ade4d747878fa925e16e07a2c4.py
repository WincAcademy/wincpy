from wincpy.checks import utils

__winc_id__ = "05b076ade4d747878fa925e16e07a2c4"


def check_stdout(student_module):
    """Running your `main.py` prints something."""
    output, _ = utils.exec_main(student_module)
    assert output != "", "Your program didn't print anything."
