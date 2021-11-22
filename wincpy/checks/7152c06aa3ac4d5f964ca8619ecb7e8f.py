from wincpy.checks import utils

__winc_id__ = "7152c06aa3ac4d5f964ca8619ecb7e8f"


def check_bool(student_module):
    """There's a `bool` in your code"""
    assert bool in __get_types_in_state(
        student_module
    ), "There's no variable with a `bool` stored in it after running your code"


def check_str(student_module):
    """There's a `str` in your code"""
    assert str in __get_types_in_state(
        student_module
    ), "There's no variable with a `str` stored in it after running your code"


def check_int(student_module):
    """There's an `int` in your code"""
    assert int in __get_types_in_state(
        student_module
    ), "There's no variable with an `int` stored in it after running your code"


def __get_types_in_state(student_module):
    return set([type(v) for v in utils.exec_main(student_module)[1].values()])
