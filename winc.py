import inspect
import sys
import os
from argparse import ArgumentParser

import style
from tests import *


def check(assignment_nr, solution_path, raise_errors=False):
    """
    Checks an assignment by assignment number.
    """
    print("""\t\t\t
█░█░█ █ █▄░█ █▀▀ █▀█ █▄█\n\
▀▄▀▄▀ █ █░▀█ █▄▄ █▀▀ ░█░\n""")

    tests = gather_tests()
    try:
        result = tests[assignment_nr](solution_path)
    except IndexError as e:
        print(f'{style.color.red}Voor deze opdracht bestaat nog geen test.{style.color.end}')
        sys.exit(1)
    report(result, raise_error=raise_errors)


def gather_tests():
    functions = inspect.getmembers(sys.modules['tests'], inspect.isfunction)
    tests = [f for fname, f in functions if fname.split('_')[0] == 'test']
    return tests


def report(result, raise_error=False):
    """
    Reports the result of the test to the student.
    """
    print(style.color.gray + 'Testresultaat' + style.color.end)
    print(style.layout.divider.level_1)
    for requirement, score, error in result:
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
            if raise_error:
                raise(error)
    print(style.layout.divider.level_1)


if __name__ == '__main__':
    parser = ArgumentParser(description='Kijkt je Winc opdrachten na.')
    parser.add_argument(dest='solution', type=str,
            help='Filename of the solution to test.')
    parser.add_argument('-t', '--traceback', action='store_true',
            help='Enable to show traceback for the first error and exit.')
    args = parser.parse_args()

    if not args.traceback:
        sys.tracebacklimit = 0

    try:
        solution_basename = os.path.basename(args.solution)
        assignment_nr = int(solution_basename.split('_')[0])
    except:
        raise ValueError("\n=========================\
                \nDe gegeven bestandsnaam is niet correct. Het format is:\
                \n\n\topdrachtnummer_opdrachtnaam.py\
                \n\nBijvoorbeeld:\
                \n\n\t00_print.py")

    if not os.path.exists(args.solution):
        raise ValueError('Het opgegeven bestand bestaat niet.')


    check(assignment_nr, args.solution, args.traceback)
