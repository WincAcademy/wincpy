import unittest
from argparse import ArgumentParser

from solution_tests import *


def check(assignment_nr):
    tests = [TestPrint, TestVariabelen, TestRekenen, TestComments]

    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(
                    tests[assignment_nr]
                )
    unittest.TextTestRunner().run(test_suite)


if __name__ == '__main__':
    parser = ArgumentParser(description='Kijkt je Winc opdrachten na.')
    parser.add_argument(dest='solution', type=str)
    args = parser.parse_args()
    try:
        assignment_nr, _ = args.solution.split('_')
        assignment_nr = int(assignment_nr)
    except:
        raise ValueError("\n=========================\
                \nDe gegeven bestandsnaam is niet correct. Het format is:\
                \n\n\topdrachtnummer_opdrachtnaam.py\
                \n\nBijvoorbeeld:\
                \n\n\t00_print.py")

    check(assignment_nr)
