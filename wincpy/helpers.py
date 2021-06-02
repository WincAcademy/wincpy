from argparse import ArgumentParser
import os
import subprocess
import sys
import urllib.request
import json
import importlib

from wincpy import style


def exec_assignment_code(filename):
    """ Execs the code in filename and returns a dictionary with the variables
    in scope minus builtins. """

    with open(filename, 'r') as fp:
        assignment_code = fp.read()

    state = {}
    print(style.color.gray
          + 'Output from running ' + os.path.split(filename)[1]
          + style.color.end)
    print(style.layout.divider.level_1)

    try:
        exec(assignment_code, state)
    except:
        print(style.color.red
              + 'Your code could not be executed successfully.\n'
              + style.color.end)
        sys.exit(1)

    print(style.layout.divider.level_1 + '\n')

    del state['__builtins__']

    try:
        output = subprocess.run(
            ['python', filename], capture_output=True, text=True
        ).stdout
    except:
        # User might have python under python3
        output = subprocess.run(
            ['python3', filename], capture_output=True, text=True
        ).stdout

    return output, state


def compare_states(expected_state, actual_state):
    """
    Takes two dicts of {var_name: var_value} and results a list of tuples
    (requirement, True/False) that represents how the two states compare.
    """

    result = []

    requirement = 'All variables are declared correctly.'
    expected_var_names = set(expected_state)
    actual_var_names = set(actual_state)
    remainder = expected_var_names - actual_var_names
    result.append((requirement, len(remainder) == 0))
    if remainder is not None:
        for key in remainder:
            result.append(
                (f'--> Something goes wrong at variable {key}.', False))

    requirement = 'All variables contain the correct values.'
    es_tupleset = set(expected_state.items())
    as_tupleset = set(actual_state.items())
    result.append((requirement, es_tupleset <= as_tupleset))
    if not result[-1][1]:
        diff = es_tupleset - as_tupleset
        for key, _ in diff:
            result.append(
                (f'{style.layout.list_item} Something is wrong with variable {key}.', False))

    return result


def get_main_abspath(module):
    try:
        main_abspath = os.path.join(module.__path__[0], 'main.py')
    except:
        main_abspath = module.__file__
    if not os.path.exists(main_abspath):
        raise FileNotFoundError
    return main_abspath


def get_iddb():
    iddb_url = 'https://raw.githubusercontent.com/WincAcademy/wincid/master/iddb.json'
    iddb_bytes = urllib.request.urlopen(iddb_url, timeout=1).read()
    iddb = json.loads(iddb_bytes)
    try:
        iddb_bytes = urllib.request.urlopen(iddb_url, timeout=1).read()
        iddb = json.loads(iddb_bytes)
    except:
        sys.stderr.write('Could not load database.\n')
        sys.exit(1)
    return iddb


def get_student_module(path):
    arg_abspath = os.path.abspath(path)
    parent_abspath, student_module_name = os.path.split(arg_abspath)
    sys.path.insert(0, arg_abspath)

    # Redirect stdout to the void while importing
    prev_stdout = sys.stdout
    devnull = open(os.devnull, 'w')
    sys.stdout = devnull

    try:
        student_module = importlib.import_module('main')
    except ImportError:
        sys.stderr.write(style.color.red
                         + f'Could not import module {student_module_name} from {parent_abspath}\n'
                         + style.color.end)
        sys.exit(1)

    if not hasattr(student_module, '__winc_id__'):
        try:
            # Try to import old-style package for backwards compatibility.
            sys.path.insert(1, parent_abspath)
            student_module = importlib.import_module(student_module_name)
        except ImportError:
            # There's just no module around here.
            sys.stderr.write(style.color.red
                             + f'Could not import module {student_module_name} from {parent_abspath}\n'
                             + style.color.end)
        if not hasattr(student_module, '__winc_id__'):
            sys.stderr.write(style.color.red
                             + 'This module does not have a Winc ID.\n'
                             + 'Is it a Winc module?\n'
                             + style.color.end)
            sys.exit(1)

    # Restore stdout
    sys.stdout = prev_stdout
    devnull.close()
    return student_module


def parse_args():
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
    return args
