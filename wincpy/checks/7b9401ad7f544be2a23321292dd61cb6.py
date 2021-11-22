""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.checks import utils
import random

__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"

RANDOM_STR = str(random.random())


def check_greet(student_module):
    name = f"Bob #{RANDOM_STR}"
    assert (
        student_module.greet(name) == f"Hello, {name}!"
    ), "The greeting for the default case is not correct."

    template = f"Testing, <name>{RANDOM_STR}!"
    assert student_module.greet(name, template) == template.replace(
        "<name>", name
    ), "The greeting with a template is not not correct."


def check_force(student_module):
    assert student_module.force(10) == 98, "Did you use earth's gravity by default?"
    assert (
        round(student_module.force(50)) == 490
    ), "Did you use earth's gravity by default?"

    assert student_module.force(10, "sun") == 2740, "'sun' is not handled correctly"
    assert student_module.force(10, "pluto") == 6, "'pluto' is not handled correctly"
    assert (
        student_module.force(10, "saturn") == 104
    ), "'saturn' is not handled correctly"
    assert student_module.force(10, "earth") == 98, "'earth' is not handled correctly"


def check_pull(student_module):
    assert student_module.pull(1, 2, 3) is not None
    assert round(student_module.pull(800, 1500, 3), 10) == 8.8987e-06
    assert (
        round(student_module.pull(0.1, 5.972 * 10 ** 4, 6.371 * 10 ** 6), 30)
        == 9.819532033e-21
    )
