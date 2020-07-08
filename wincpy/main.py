import importlib
import inspect
import os
import shutil
import sys
from argparse import ArgumentParser

from wincpy import helpers, solutions, starts, style, tests


def main(stdout, stderr):
    parser = ArgumentParser(description='The Winc Python tool.')
    subparsers = parser.add_subparsers(dest='action',
                                       help='What wincpy should do in this run.')
    start_parser = subparsers.add_parser('start',
                                         help='Start a new assignment.')
    check_parser = subparsers.add_parser('check',
                                         help='Check an existing assignment.')

    start_parser.add_argument('winc_id', type=str,
                              help='Winc ID of an assignment to start.')
    check_parser.add_argument('path', type=str,
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
        sys.stderr.write("Unknown Winc ID; can't start assignment.\n")
        sys.exit(1)

    human_name = iddb[args.winc_id]['human_name']
    print(f'Starting assignment {human_name} with ID {args.winc_id}')

    starts_abspath = starts.__path__[0]
    starts_dirs = list(os.walk(starts_abspath))[0][1]
    starts_dirs = {d: os.path.join(starts_abspath, d) for d in starts_dirs}

    # Winc ID is known, but does not require a particular start.
    if args.winc_id not in starts_dirs:
        try:
            shutil.copytree(starts_dirs['tabula_rasa'], human_name)
        except:
            sys.stderr.write(
                f"Error: could not create directory {human_name}. Exiting.")
        with open(os.path.join(human_name, '__init__.py'), 'w') as fp:
            fp.write(f"__winc_id__ = '{args.winc_id}'\n")
            fp.write(f"__human_name__ = '{human_name}'")
    else:
        try:
            shutil.copytree(starts_dirs[args.winc_id], human_name)
        except:
            sys.stderr.write(
                f"Error: could not create directory {human_name}. Exiting.\n")
    print('Done.')


def check(args):
    try:
        sys.path.insert(1, os.getcwd())
        student_module = importlib.import_module(args.path)
    except:
        sys.stderr.write(f'{style.color.red}Could not import a module from {args.path}{style.color.end}\n')
        sys.exit(1)

    try:
        test = importlib.import_module(f'.{student_module.__winc_id__}', 'wincpy.tests')
    except ImportError:
        sys.stderr.write(f'{style.color.red}There is no test for this assignment yet.{style.color.end}\n')
        sys.exit(1)

    result = test.run(student_module)

    return result


def report(result):
    """
    Reports the result of the test to the student.
    """
    print(style.color.gray + 'Testresultaat' + style.color.end)
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
