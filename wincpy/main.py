import importlib
import inspect
import os
import shutil
import subprocess

import wincpy
from wincpy import helpers, ui, starts, checks, solutions


def main(stdout, stderr):
    args = helpers.parse_args()
    ui.print_intro()

    if args.action == "start":
        start(args)
    elif args.action == "check":
        result = check(args)
        ui.report_check_result(result)
        if all([score for _, score in result]):
            exit(0)
        else:
            # No runtime errors but the solution didn't pass.
            exit(1)
    elif args.action == "update":
        update()
    elif args.action == "solve":
        result = check(args)
        passed = all([x for _, x in result])
        if passed:
            solve(args)
        else:
            ui.report_error("solve_first")
            exit(1)
    elif args.action == "version":
        ui.print_version()


def start(args):
    iddb = helpers.get_iddb()
    if args.winc_id not in iddb:
        ui.report_error("unknown_winc_id")
        exit(2)

    human_name = iddb[args.winc_id]["human_name"]
    ui.report_neutral("assignment_start", assignment_name=human_name)

    starts_abspath = starts.__path__[0]
    starts_dirs = list(os.walk(starts_abspath))[0][1]
    starts_dirs = {d: os.path.join(starts_abspath, d) for d in starts_dirs}

    # Winc ID is known, but does not require a particular start.
    if args.winc_id not in starts_dirs:
        try:
            os.mkdir(human_name)
        except FileExistsError:
            ui.report_error("dir_exists", dirname=human_name)
            exit(3)
        with open(os.path.join(human_name, "main.py"), "w") as fp:
            fp.write(
                "# Do not modify these lines\n"
                + f"__winc_id__ = '{args.winc_id}'\n"
                + f"__human_name__ = '{human_name}'\n\n"
                + "# Add your code after this line\n"
            )
    else:
        try:
            shutil.copytree(starts_dirs[args.winc_id], human_name)
        except FileExistsError:
            ui.report_error("dir_exists", dirname=human_name)
            exit(3)
    ui.report_success("assignment_start", assignment_name=human_name)


def check(args):
    student_module = helpers.get_student_module(args.path)

    winc_id = student_module.__winc_id__
    try:
        check_module = importlib.import_module(f".{winc_id}", "wincpy.checks")
        # solution_module = importlib.import_module(f'.{winc_id}', 'wincpy.solutions')
    except ImportError:
        ui.report_error("no_check_found", assignment_name=student_module.__human_name__)
        exit(4)

    checks = [v for k, v in check_module.__dict__.items() if k.startswith("check_")]
    if not checks:
        ui.report_error("empty_check", assignment_name=student_module.__human_name__)
    result = []
    for check in checks:
        if not check.__doc__:
            fname = check.__qualname__
            check.__doc__ = (
                "`" + fname[fname.find("_") + 1 :] + "` is implemented correctly"
            )
        try:
            check(student_module)
            result.append((check.__doc__, None))
        except Exception as e:
            result.append((check.__doc__, e))
    return result


def update():
    release_url = "git+https://github.com/WincAcademy/wincpy@release"
    args = ["python3", "-m", "pip", "install", release_url, "--upgrade"]
    try:
        subprocess.run(args, check=True)
    except:
        args[0] = "python"
        subprocess.run(args, check=True)


def solve(args):
    student_module = helpers.get_student_module(args.path)
    winc_id = student_module.__winc_id__

    solutions_abspath = solutions.__path__[0]
    solution_abspath = os.path.join(solutions_abspath, winc_id)
    if not os.path.isdir(solution_abspath):
        ui.report_error(
            "no_solution_available", exercise_name=student_module.__human_name__
        )
        exit(5)

    try:
        dest_dir = student_module.__human_name__ + "_example_solution"
        shutil.copytree(solution_abspath, dest_dir)
        ui.report_success("solution_available", solution_dir=dest_dir)
    except:
        ui.report_error("dir_exists", dirname=dest_dir)
        exit(3)
