import importlib
import inspect
import os
import shutil
import sys
from argparse import ArgumentParser

from wincpy import helpers, solutions, starts, style, tests


def main(stdout, stderr):
    parser = ArgumentParser(description='The Winc Python tool.')
    subparsers = parser.add_subparsers(dest='action', required=True,
                                       help='What wincpy should do in this run.')
    start_parser = subparsers.add_parser('start',
                                         help='Start a new assignment.')
    check_parser = subparsers.add_parser('check',
                                         help='Check an existing assignment.')

    start_parser.add_argument('winc_id', type=str,
                              help='Winc ID of an assignment to start.')
    check_parser.add_argument('path', type=str, nargs='?', default=os.getcwd(),
                              help='Path containing assignment to check.')

    args = parser.parse_args()

    print(style.misc.logo)

    if args.action == 'start':
        start(args)
    elif args.action == 'check':
        result = check(args)
        report(result)


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
            shutil.copytree(starts_dirs['tabula_rasa'], human_name)
        except:
            sys.stderr.write(
                f"{style.color.red}Error: could not create directory '{human_name}'. Exiting.\n{style.color.end}")
            sys.exit(1)
        with open(os.path.join(human_name, '__init__.py'), 'w') as fp:
            fp.write(f"__winc_id__ = '{args.winc_id}'\n")
            fp.write(f"__human_name__ = '{human_name}'")
    else:
        try:
            shutil.copytree(starts_dirs[args.winc_id], human_name)
        except:
            sys.stderr.write(
                f"Error: could not create directory {human_name}. Exiting.\n")
            sys.exit(1)
    print(f'You can find the assignment files in the directory: {human_name}')


def check(args):
    arg_abspath = os.path.abspath(args.path)
    sys.path.insert(1, arg_abspath)

    try:
        student_module = importlib.import_module('main')
    except ImportError:
        sys.stderr.write(style.color.red
                        + f'Could not import module {student_module_name} from {parent_abspath}\n'
                        + style.color.end)
        sys.exit(1)
    try:
        winc_id = student_module.__winc_id__
    except AttributeError:
        try:
            """ This block exists for backwards compatibility. Can be removed
            iff all starts and all solutions are no longer structured as a
            package with an __init__.py but simple folders with a main.py
            entrypoint. """
            parent_abspath, student_module_name = os.path.split(arg_abspath)
            sys.path.insert(1, parent_abspath)
            student_module = importlib.import_module(student_module_name)
            winc_id = student_module.__winc_id__
        except ImportError:
            sys.stderr.write(style.color.red
                            + f'Could not import module {student_module_name} from {parent_abspath}\n'
                            + style.color.end)
        except AttributeError:
            sys.stderr.write(style.color.red
                             + 'This module does not have a Winc ID.\n'
                             + 'Is it a Winc module?\n'
                             + style.color.end)
            sys.exit(1)

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
