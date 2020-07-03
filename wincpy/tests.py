import subprocess

from wincpy.helpers import exec_assignment_code


def test_print(filename='00_print.py'):
    result = []

    output = subprocess.run(
        ['python', filename], capture_output=True, text=True
    ).stdout

    requirement = 'Er wordt iets geprint.'
    result.append((requirement, output != ''))

    return result


def test_variabelen(filename='01_variabelen.py'):
    result = []

    assignment_state = exec_assignment_code(filename)
    types_in_state = [type(var) for var in assignment_state.values()]

    requirement = 'Er wordt een bool gedeclareerd.'
    result.append((requirement, bool in types_in_state))

    requirement = 'Er wordt een string gedeclareerd.'
    result.append((requirement, str in types_in_state))

    requirement = 'Er wordt een int gedeclareerd.'
    result.append((requirement, int in types_in_state))

    return result
