from wincpy.checks import utils
from wincpy.checks.utils import StandardChecks

__winc_id__ = "49bce82ef9cc475ca3146ee15b0259d0"


def check_greet(student_module):
    StandardChecks.n_params(student_module.greet, n_params=1)

    assert student_module.greet("Bob") == "Hello, Bob!"
    assert student_module.greet("Fred") == "Hello, Fred!"


def check_add(student_module):
    StandardChecks.n_params(student_module.add, n_params=3)

    assert student_module.add(5, 1, 4) == 10, "A tested addition was incorrect"
    assert student_module.add(1, 1, 9) == 11, "A tested addition was incorrect"


def check_positive(student_module):
    StandardChecks.n_params(student_module.positive, n_params=1)

    assert student_module.positive(5) is True
    assert student_module.positive(-5) is False
    assert student_module.positive(0) is False


def check_negative(student_module):
    StandardChecks.n_params(student_module.negative, n_params=1)

    assert student_module.negative(5) is False
    assert student_module.negative(-5) is True
    assert student_module.negative(0) is False
