import subprocess

from helpers import exec_assignment_code


def test_print(filename='00_print.py'):
    result = []

    process = subprocess.run(
        ['python', filename], capture_output=True, text=True
    )
    try:
        assert process.stdout != '', 'Er wordt niets geprint.'
    except AssertionError as e:
        result.append(e)

    return result


def test_variabelen(filename='01_variabelen.py'):
    result = []

    assignment_state = exec_assignment_code(filename)
    types_in_state = [type(var) for var in assignment_state.values()]

    requirement = 'Er wordt een bool gedeclareerd.'
    try:
        assert bool in types_in_state
        result.append((requirement, True, None))
    except AssertionError as e:
        result.append((requirement, False, e))

    requirement = 'Er wordt een string gedeclareerd.'
    try:
        assert str in types_in_state
        result.append((requirement, True, None))
    except AssertionError as e:
        result.append((requirement, False, e))

    requirement = 'Er wordt een int gedeclareerd.'
    try:
        assert int in types_in_state
        result.append((requirement, True, None))
    except AssertionError as e:
        result.append((requirement, False, e))

    return result
