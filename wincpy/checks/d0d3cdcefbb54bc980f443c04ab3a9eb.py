""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.checks import utils

__winc_id__ = "d0d3cdcefbb54bc980f443c04ab3a9eb"


def check_output(student_module):
    """All output is as expected"""
    # TODO: FEATURE: check if the correct operators have been used in addition
    # to just checking the result.
    output, state = utils.exec_main(student_module)

    expected = [str(x) for x in [False, True, False, True, True, True, True]]
    output = output.split("\n")
    assert len(output) == len(
        expected
    ), f"Output was expected to be `{len(expected)}` lines long but was `{len(output)}` lines."

    for i, (o, e) in enumerate(zip(output, expected)):
        assert o == e, f"Output line {i} should be {e} but was {o}"
