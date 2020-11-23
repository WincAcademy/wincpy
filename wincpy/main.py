import importlib
import inspect
import os
import shutil
import sys
from argparse import ArgumentParser
import subprocess

from wincpy import helpers, solutions, starts, style, tests


def main(stdout, stderr):
    parser = ArgumentParser(description='The Winc Python tool.')
    subparsers = parser.add_subparsers(dest='action', required=True,
                                       help='What wincpy should do in this run.')
    start_parser = subparsers.add_parser('start',
                                         help='Start a new assignment.')
    check_parser = subparsers.add_parser('check',
                                         help='Check an existing assignment.')
    solve_parser = subparsers.add_parser('solve',
                                         help="Place Winc's solution here.")

    # Update parser doesn't have any extra arguments, but we must add it as
    # subparser to have it available as an actions together with the rest.
    update_parser = subparsers.add_parser('update',
                                         help='Update wincpy using pip.')

    start_parser.add_argument('winc_id', type=str,
                              help='Winc ID of an assignment to start.')
    check_parser.add_argument('path', type=str, nargs='?', default=os.getcwd(),
                              help='Path containing assignment to check.')
    solve_parser.add_argument('path', type=str, nargs='?', default=os.getcwd(),
                              help='Path containing assignment to check.')

    args = parser.parse_args()

    print(style.misc.logo)

    if args.action == 'start':
        start(args)
    elif args.action == 'check':
        result = check(args)
        report(result)
    elif args.action == 'update':
        update()
    elif args.action == 'solve':
        result = check(args)
        passed = sum([x for _, x in result]) == len(result)
        if passed:
            solve(args)
        else:
            sys.stdout.write(style.color.red
                             + "You should solve the exercise before viewing Winc's solution."
                             + style.color.end)
            sys.exit(1)


def start(args):
    iddb = helpers.get_iddb()
    if args.winc_id not in iddb:
        sys.stderr.write(style.color.red
                         + "Unknown Winc ID; can't start assignment.\n"
                         + style.color.end)
        sys.exit(1)

    human_name = iddb[args.winc_id]['human_name']
    print(f'{style.color.green}Starting assignment: {human_name}{style.color.end}\n'
          + f'Winc ID: {args.winc_id}')

    starts_abspath = starts.__path__[0]
    starts_dirs = list(os.walk(starts_abspath))[0][1]
    starts_dirs = {d: os.path.join(starts_abspath, d) for d in starts_dirs}

    # Winc ID is known, but does not require a particular start.
    if args.winc_id not in starts_dirs:
        try:
            os.mkdir(human_name)
        except:
            sys.stderr.write(
                f"{style.color.red}Error: could not create directory '{human_name}'. Exiting.\n{style.color.end}")
            sys.exit(1)
        with open(os.path.join(human_name, 'main.py'), 'w') as fp:
            fp.write('# Do not modify these lines\n'
                     + f"__winc_id__ = '{args.winc_id}'\n"
                     + f"__human_name__ = '{human_name}'\n\n"
                     + '# Add your code after this line\n')
    else:
        try:
            shutil.copytree(starts_dirs[args.winc_id], human_name)
        except:
            sys.stderr.write(
                f"Error: could not create directory {human_name}. Exiting.\n")
            sys.exit(1)
    print(f'You can find your starting files in the directory: {human_name}')


def check(args):
    student_module = helpers.get_student_module(args.path)

    winc_id = student_module.__winc_id__
    try:
        test = importlib.import_module(f'.{winc_id}', 'wincpy.tests')
        # solution_module = importlib.import_module(f'.{winc_id}', 'wincpy.solutions')
    except ImportError:
        sys.stderr.write(style.color.red
                         + 'There is no test for this assignment yet.\n'
                         + style.color.end)
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
