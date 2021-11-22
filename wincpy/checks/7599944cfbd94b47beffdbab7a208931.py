from wincpy.checks import utils

__winc_id__ = "7599944cfbd94b47beffdbab7a208931"


def check_state(student_module):
    """All the variables are named and filled in as expected"""
    _, state = utils.exec_main(student_module)
    expected_state = {k: True for k in ["one", "two", "three"]}
    utils.check_state(expected_state, state)
