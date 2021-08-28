from argparse import ArgumentParser
import os
import subprocess
import sys
import urllib.request
import json
import importlib

from wincpy import ui


def exec_assignment_code(filename, quiet=False):
    """
    Execs the code in filename and returns a dictionary with the variables
    in scope minus builtins.
    """

    with open(filename, "r") as fp:
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
            ["python", filename], capture_output=True, text=True
        ).stdout
    except:
        # User might have python under python3
        output = subprocess.run(
            ["python3", filename], capture_output=True, text=True
        ).stdout

    if not quiet:
        ui.print_student_output(output)
    return output, state


def compare_states(expected_state, actual_state):
    """
    Takes two dicts of {var_name: var_value} and results a list of tuples
    (requirement, True/False) that represents how the two states compare.
    """

    result = []

    requirement = "All variables are declared correctly."
    expected_var_names = set(expected_state)
    actual_var_names = set(actual_state)
    remainder = expected_var_names - actual_var_names
    result.append((requirement, len(remainder) == 0))
    if remainder is not None:
        for key in remainder:
            result.append((f"--> Something goes wrong at variable {key}.", False))

    requirement = "All variables contain the correct values."
    es_tupleset = set(expected_state.items())
    as_tupleset = set(actual_state.items())
    result.append((requirement, es_tupleset <= as_tupleset))
    if not result[-1][1]:
        diff = es_tupleset - as_tupleset
        for key, _ in diff:
            result.append(
                (
                    f"{style.layout.list_item} Something is wrong with variable {key}.",
                    False,
                )
            )
    return result


def get_main_abspath(module):
    try:
        main_abspath = os.path.join(module.__path__[0], "main.py")
    except:
        main_abspath = module.__file__
    if not os.path.exists(main_abspath):
        raise FileNotFoundError
    return main_abspath


def get_iddb():
    iddb_url = "https://raw.githubusercontent.com/WincAcademy/wincid/master/iddb.json"
    iddb_bytes = urllib.request.urlopen(iddb_url, timeout=1).read()
    iddb = json.loads(iddb_bytes)
    try:
        iddb_bytes = urllib.request.urlopen(iddb_url, timeout=1).read()
        iddb = json.loads(iddb_bytes)
    except:
        ui.report_error("iddb_load_fail")
        exit(6)
    return iddb


def get_student_module(path):
    arg_abspath = os.path.abspath(path)
    parent_abspath, student_module_name = os.path.split(arg_abspath)
    sys.path.insert(0, arg_abspath)

    # Redirect stdout to the void while importing
    ui.mute_stdout()
    try:
        student_module = importlib.import_module("main")
    except ImportError:
        ui.unmute_stdout()
        ui.report_error(
            "module_import_fail", module_name=student_module_name, dir=parent_abspath
        )
        exit(51)

    if not hasattr(student_module, "__winc_id__"):
        ui.unmute_stdout()
        ui.report_error(
            "module_no_winc_id", module_name=student_module_name, dir=parent_abspath
        )
        exit(52)

    # Restore stdout
    ui.unmute_stdout()
    return student_module


def parse_args():
    parser = ArgumentParser(description="The Winc Python tool.")
    subparsers = parser.add_subparsers(
        dest="action", required=True, help="What wincpy should do in this run."
    )
    start_parser = subparsers.add_parser("start", help="Start a new assignment.")
    check_parser = subparsers.add_parser("check", help="Check an existing assignment.")
    solve_parser = subparsers.add_parser("solve", help="Place Winc's solution here.")

    # Update parser doesn't have any extra arguments, but we must add it as
    # subparser to have it available as an actions together with the rest.
    update_parser = subparsers.add_parser("update", help="Update wincpy using pip.")

    start_parser.add_argument(
        "winc_id", type=str, help="Winc ID of an assignment to start."
    )
    check_parser.add_argument(
        "path",
        type=str,
        nargs="?",
        default=os.getcwd(),
        help="Path containing assignment to check.",
    )
    solve_parser.add_argument(
        "path",
        type=str,
        nargs="?",
        default=os.getcwd(),
        help="Path containing assignment to check.",
    )

    args = parser.parse_args()
    return args
