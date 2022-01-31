""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

import time
import math
from datetime import datetime as dt
import random
import sys

from wincpy.checks import utils
from wincpy.checks.utils import StandardChecks

__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"


def check_zen(student_module):
    """The Zen of Python is imported"""
    "import this" in utils.get_main_src(student_module)


def check_wait(student_module):
    StandardChecks.n_params(student_module.wait, n_params=1)

    wait_duration = random.random()
    start = time.time()
    student_module.wait(wait_duration)
    actual_duration = time.time() - start
    assert round(actual_duration, 1) == round(
        wait_duration, 1
    ), f"Expected to wait for {wait_duration} but actually waited for {actual_duration}"


def check_my_sin(student_module):
    StandardChecks.n_params(student_module.my_sin, n_params=1)

    assert student_module.my_sin(math.pi / 2) == 1
    assert student_module.my_sin(3 / 2 * math.pi) == -1


def check_iso_now(student_module):
    StandardChecks.n_params(student_module.iso_now, n_params=0)

    # It's possible that the test occurs right on both sides of the minute
    # changeover, but unlikely.. enough.
    assert student_module.iso_now() == dt.now().strftime("%Y-%m-%dT%H:%M")


def check_platform(student_module):
    StandardChecks.n_params(student_module.platform, n_params=0)

    expected_platform = sys.platform
    platform = student_module.platform()
    assert (
        student_module.platform() == sys.platform
    ), f"Expected platform to be {expected_platform}, but it was {platform}"


def check_supergreeting_wrapper(student_module):
    StandardChecks.n_params(student_module.supergreeting_wrapper, n_params=1)
    assert student_module.supergreeting_wrapper("Winc") == "Hellooo...ooo, Winc!"
