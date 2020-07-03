import subprocess

from wincpy import style
from wincpy.helpers import compare_states, exec_assignment_code


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

    output = subprocess.run(
            ['python', filename], capture_output=True, text=True
            ).stdout

    assignment_state = exec_assignment_code(filename)
    result += compare_states(expected_state, assignment_state)

    requirement = 'Het eindberag klopt.'
    result.append((requirement, float(output) == 66.5))

    return result


def test_003_comments(filename='03_comments.py'):
    result = []

    assignment_text = open(filename).read()
    assignment_state = exec_assignment_code(filename)

    requirement = 'De oplossing bevat twee end-of-line comments.'
    end_of_line_comment_count = 0
    for line in assignment_text.split('\n'):
        line = line.replace(' ', '')
        try:
            hash_index = line.index('#')
            if hash_index > 0:
                end_of_line_comment_count += 1
        except ValueError:
            # No comment on this line
            pass
    result.append((requirement, end_of_line_comment_count >= 2))

    requirement = 'De oplossing bevat twee single-line comments.'
    single_line_comment_count = 0
    for line in assignment_text.split('\n'):
        line = line.replace(' ', '')
        if line != '' and line[0] == '#':
            single_line_comment_count += 1
    result.append((requirement, single_line_comment_count >= 2))

    requirement = 'De oplossing bevat twee multiline comments.'
    multiline_comment_count = 0
    for line in assignment_text.split('\n'):
        line = line.replace(' ', '')
        # If we're here, we already ran the code, so the multiline comment
        # is also properly terminated somewhere.
        if line != '' and line[0:3] == '"""':
            multiline_comment_count += 1
    result.append((requirement, multiline_comment_count >= 2))

    return result
