import inspect
import os
import sys
from argparse import ArgumentParser

from wincpy import style, tests, helpers
# import style
# from tests import *

def main(stdout, stderr):
    parser = ArgumentParser(description='Kijkt je Winc opdrachten na.')
    parser.add_argument(dest='solution', type=str,
                        help='Filename of the solution to test.')
    # parser.add_argument('-t', '--traceback', action='store_true',
                        # help='Enable to show traceback for the first error and exit.')
    args = parser.parse_args()

    print("""\t\t\t
█░█░█ █ █▄░█ █▀▀ █▀█ █▄█\n\
▀▄▀▄▀ █ █░▀█ █▄▄ █▀▀ ░█░\n""")


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

    result = check(assignment_nr, args.solution)
    report(result)


def check(assignment_nr, solution_path):
    """
    Checks an assignment by assignment number.
    """
    tests = gather_tests()
    try:
        result = tests[assignment_nr](solution_path)
    except IndexError:
        print(
            f'{style.color.red}Voor deze opdracht bestaat nog geen test.{style.color.end}')
        sys.exit(1)
    return result


def gather_tests():
    functions = inspect.getmembers(sys.modules['wincpy.tests'], inspect.isfunction)
    tests = [f for fname, f in functions if fname.split('_')[0] == 'test']
    return tests


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
