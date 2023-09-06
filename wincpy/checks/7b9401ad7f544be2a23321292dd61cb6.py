""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

import random

from wincpy.checks import utils
from wincpy.checks.utils import StandardChecks

__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"

RANDOM_STR = str(random.random())


def check_greet(student_module):
    StandardChecks.n_params(student_module.greet, n_params=2, count_optionals=True)
    name = f"Bob #{RANDOM_STR}"
    assert (
        student_module.greet(name) == f"Hello, {name}!"
    ), "The greeting for the default case is not correct."

    template = f"Testing, <name>{RANDOM_STR}!"
    assert student_module.greet(name, template) == template.replace(
        "<name>", name
    ), "The greeting with a template is not correct."


def check_force(student_module):
    StandardChecks.n_params(student_module.force, n_params=2, count_optionals=True)

    assert student_module.force(10) == 98 or 97.98, "Did you use earth's gravity by default?"
    assert (
        round(student_module.force(20)) == 196 or 195.96
    ), "Did you use earth's gravity by default?"

    assert student_module.force(10, "pluto") == 6.0 or 5.8, "'pluto' is not handled correctly"
    assert student_module.force(10, "saturn") == 104, "'saturn' is not handled correctly"
    assert student_module.force(10, "earth") == 98, "'earth' is not handled correctly"
    assert (
        student_module.force(10, "jupiter") == 249
    ), "'jupiter' is not handled correctly"
    assert (
        student_module.force(10, "neptune") == 112
    ), "'neptune' is not handled correctly"
    assert student_module.force(10, "moon") == 16, "'moon' is not handled correctly"


def check_pull(student_module):
    StandardChecks.n_params(student_module.pull, n_params=3)
    assert student_module.pull(1, 2, 3) is not None
    assert round(student_module.pull(800, 1500, 3), 10) == 8.8987e-06
    assert (
        round(student_module.pull(0.1, 5.972 * 10**4, 6.371 * 10**6), 30)
        == 9.819532033e-21
    )
