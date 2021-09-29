import os
import subprocess

from wincpy import ui


def execute_module_main(module, quiet=True):
    """Executes the code in the module's ``main.py`` and returns a dictionary
    with the variables in scope minus builtins.
    """
    try:
        main_abspath = os.path.join(module.__path__[0], "main.py")
    except:
        main_abspath = module.__file__
    if not os.path.exists(main_abspath):
        raise FileNotFoundError

    with open(main_abspath, "r") as fp:
        assignment_code = fp.read()

    try:
        ui.mute_stdout()
        state = {}
        exec(assignment_code, state)
        ui.unmute_stdout()
    except:
        ui.unmute_stdout()
        ui.report_error("exec_failed")
        exit(50)

    del state["__builtins__"]

    try:
        output = subprocess.run(
            ["python3", main_abspath], capture_output=True, text=True
        ).stdout
    except:
        # User might have python3 under python
        output = subprocess.run(
            ["python", main_abspath], capture_output=True, text=True
        ).stdout

    if not quiet:
        ui.print_student_output(output)
    return output, state


def check_state(expected_state, actual_state):
    for k, v in expected_state.items():
        assert (
            k in actual_state.keys()
        ), f"We expected `{k}` to be a variable in your program"
        assert (
            expected_state[k] == actual_state[k]
        ), f"We expected `{k}` to be `{expected_state[k]}` but it was `{actual_state[k]}`"
