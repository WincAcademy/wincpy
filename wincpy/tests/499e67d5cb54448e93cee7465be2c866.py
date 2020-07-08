import subprocess

from wincpy.helpers import exec_assignment_code, compare_states, get_main_abspath

__winc_id__ = '499e67d5cb54448e93cee7465be2c866'


def run(student_module):
    result = []
    main_abspath = get_main_abspath(student_module)

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

    output, assignment_state = exec_assignment_code(main_abspath)
    result += compare_states(expected_state, assignment_state)

    requirement = 'Het eindberag klopt.'
    result.append((requirement, float(output) == 66.5))

    return result
