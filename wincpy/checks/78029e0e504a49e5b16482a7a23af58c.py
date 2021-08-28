""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

import time
import math
from datetime import datetime as dt
import sys

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"


# Test student module
def run(sm):
    result = []

    requirement = "Zen of Python is imported"
    main_abspath = get_main_abspath(sm)
    src = open(main_abspath, "r").read()
    result.append((requirement, "import this" in src))

    requirement = "wait halts for the specified number of seconds"
    start = time.time()
    sm.wait(1.3)
    result.append((requirement, round(time.time() - start, 1) == 1.3))

    requirement = "my_sin returns sin(x)"
    result.append(
        (requirement, sm.my_sin(math.pi / 2) == 1 and sm.my_sin(3 / 2 * math.pi) == -1)
    )

    # It's possible that the test occurs right on both sides of the minute
    # changeover, but.. Unlikely.
    requirement = "iso_now is correct"
    result.append((requirement, dt.now().strftime("%Y-%m-%dT%H:%M")))

    requirement = "platform is correct"
    result.append((requirement, sm.platform() == sys.platform))

    requirement = "supergreeting_wrapper is correct"
    result.append(
        (requirement, sm.supergreeting_wrapper("Winc") == "Hellooo...ooo, Winc!")
    )

    return result
