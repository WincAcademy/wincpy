from argparse import ArgumentParser
from contextlib import redirect_stdout
import io
import os
import subprocess
import sys
import urllib.request
import json
import importlib

from wincpy import ui


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
    except Exception as e:
        ui.unmute_stdout()
        ui.report_error(
            "module_import_fail",
            module_name=student_module_name,
            dir=parent_abspath,
            exception=str(e),
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
