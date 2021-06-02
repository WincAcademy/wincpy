import importlib
import inspect
import os
import shutil
import sys
import subprocess

from wincpy import helpers, solutions, starts, style, checks, ui


def main(stdout, stderr):
    args = helpers.parse_args()
    print(style.misc.logo)

    if args.action == 'start':
        start(args)
    elif args.action == 'check':
        result = check(args)
        report(result)
        if all([score for _, score in result]):
            sys.exit(0)
        else:
            # No runtime errors but the solution didn't pass.
            sys.exit(2)
    elif args.action == 'update':
        update()
    elif args.action == 'solve':
        result = check(args)
        passed = all([x for _, x in result])
        if passed:
            solve(args)
        else:
            ui.report_error('solve_first')
            sys.exit(1)


def start(args):
    iddb = helpers.get_iddb()
    if args.winc_id not in iddb:
        ui.report_error('unknown_winc_id')
        sys.exit(1)

    human_name = iddb[args.winc_id]['human_name']
    ui.report_neutral('assignment_start', assignment_name=human_name)

    starts_abspath = starts.__path__[0]
    starts_dirs = list(os.walk(starts_abspath))[0][1]
    starts_dirs = {d: os.path.join(starts_abspath, d) for d in starts_dirs}

    # Winc ID is known, but does not require a particular start.
    if args.winc_id not in starts_dirs:
        try:
            os.mkdir(human_name)
        except FileExistsError:
            ui.report_error('dir_exists', dirname=human_name)
            sys.exit(1)
        with open(os.path.join(human_name, 'main.py'), 'w') as fp:
            fp.write('# Do not modify these lines\n'
                     + f"__winc_id__ = '{args.winc_id}'\n"
                     + f"__human_name__ = '{human_name}'\n\n"
                     + '# Add your code after this line\n')
    else:
        try:
            shutil.copytree(starts_dirs[args.winc_id], human_name)
        except FileExistsError:
            ui.report_error('dir_exists', dirname=human_name)
            sys.exit(1)
    ui.report_success('assignment_start', assignment_name=human_name)


def check(args):
    student_module = helpers.get_student_module(args.path)

    winc_id = student_module.__winc_id__
    try:
        test = importlib.import_module(f'.{winc_id}', 'wincpy.checks')
        # solution_module = importlib.import_module(f'.{winc_id}', 'wincpy.solutions')
    except ImportError:
        ui.report_error('no_check_found', assignment_name=student_module.__human_name__)
        sys.exit(1)

    # result = test.run(student_module, solution_module)
    result = test.run(student_module)

    return result


def report(result):
    """
    Reports the result of the test to the student.
    """
    print(style.color.gray + 'Test result' + style.color.end)
    print(style.layout.divider.level_1)
    for requirement, score in result:
        if score:
            sys.stdout.write(
                style.color.green
                + style.icon.thumbsup
                + requirement
                + '\n'
                + style.color.end)
        else:
            sys.stdout.write(
                style.color.red
                + style.icon.thumbsdown
                + requirement
                + '\n'
                + style.color.end)
    print(style.layout.divider.level_1)


def update():
    release_url = 'git+https://github.com/WincAcademy/wincpy@release'
    subprocess.run(['pip', 'install', release_url, '--user', '--upgrade'],
                   check=True)


def solve(args):
    student_module = helpers.get_student_module(args.path)
    winc_id = student_module.__winc_id__

    solutions_abspath = solutions.__path__[0]
    solution_abspath = os.path.join(solutions_abspath, winc_id)
    if not os.path.isdir(solution_abspath):
        sys.stderr.write(style.color.red
                         + 'There is no solution available for this exercise.\n'
                         + style.color.end)
        sys.exit(1)

    try:
        dest_dir = student_module.__human_name__ + '_example_solution'
        shutil.copytree(solution_abspath, dest_dir)
        sys.stdout.write(style.color.green
                         + f'You can now find the example solution in {dest_dir}\n'
                         + style.color.end)
    except:
        sys.stderr.write(style.color.red
                         + f'Unable to write solution to folder {dest_dir}\n'
                         + style.color.end)
        sys.exit(1)
