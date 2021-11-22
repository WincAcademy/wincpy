from contextlib import redirect_stdout
import io
import os
import subprocess
from typing import Dict, Tuple

from wincpy import ui

cache = {}


def exec_main(module, quiet=False) -> Tuple[str, Dict]:
    main_abspath = get_main_abspath(module)
    output, state = exec_assignment_code(main_abspath)
    return output.strip(), state


def exec_assignment_code(filename, quiet=False, skip_cache=False):
    """
    Execs the code in filename and returns a dictionary with the variables
    in scope minus builtins.
    """

    if not skip_cache and cache.get("output", None) and cache.get("state", None):
        return cache["output"], cache["state"]

    with open(filename, "r") as fp:
        assignment_code = fp.read()

    try:
        f = io.StringIO()
        with redirect_stdout(f):
            state = {}
            exec(assignment_code, state)
            del state["__builtins__"]
        output = f.getvalue()
    except:
        ui.report_error("exec_failed")
        exit(50)

    if not quiet:
        ui.print_student_output(output)
    cache["output"], cache["state"] = output, state
    return output, state


def get_main_abspath(module):
    try:
        main_abspath = os.path.join(module.__path__[0], "main.py")
    except:
        main_abspath = module.__file__
    if not os.path.exists(main_abspath):
        raise FileNotFoundError
    return main_abspath


def check_state(expected_state, actual_state):
    for k, v in expected_state.items():
        assert (
            k in actual_state.keys()
        ), f"We expected `{k}` to be a variable in your program"
        assert (
            expected_state[k] == actual_state[k]
        ), f"We expected `{k}` to be `{expected_state[k]}` but it was `{actual_state[k]}`"


def get_main_src(student_module):
    with open(get_main_abspath(student_module), "r") as f:
        return f.read()
