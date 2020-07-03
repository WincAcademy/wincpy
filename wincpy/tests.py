import subprocess

from wincpy.helpers import exec_assignment_code, compare_states
from wincpy import style


def test_000_print(filename='00_print.py'):
    result = []

    output = subprocess.run(
        ['python', filename], capture_output=True, text=True
    ).stdout

    requirement = 'Er wordt iets geprint.'
    result.append((requirement, output != ''))

    return result


def test_001_variabelen(filename='01_variabelen.py'):
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


def test_002_rekenen(filename='02_rekenen.py'):
    result = []
    expected_state = {
        'prei': 2,
        'aardappel': 3,
        'spruitje': 7,
        'totaal': 12,
        'gemiddelde_prijs': 4.0,
        'aantal_prei': 2,
        'aantal_aardappel': 7,
        'aantal_spruitje': 10,
        'totaal_prijs': 95,
        'korting_percentage': 30,
        'totaal_prijs_met_korting_afgerond': 66.5}

    assignment_state = exec_assignment_code(filename)
    result += compare_states(expected_state, assignment_state)

    return result
