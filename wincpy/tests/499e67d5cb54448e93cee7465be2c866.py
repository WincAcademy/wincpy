import subprocess

from wincpy.helpers import exec_assignment_code, compare_states, get_main_abspath

__winc_id__ = '499e67d5cb54448e93cee7465be2c866'


def run(student_module):
    result = []
    main_abspath = get_main_abspath(student_module)

    expected_state = {
        'broccoli': 2,
        'leek': 2,
        'potato': 3,
        'brussel_sprout': 7,
        'sum_one_each': 14,
        'avg_price': 3.5,
        'num_broccoli': 5,
        'num_leek': 2,
        'num_potato': 7,
        'num_brussel_sprout': 10,
        'sum_total': 105,
        'discount_percentage': 30,
        'discounted_sum_total': 73.5}

    output, assignment_state = exec_assignment_code(main_abspath)
    result += compare_states(expected_state, assignment_state)

    requirement = 'You printed the correct discounted sum total.'
    try:
        result.append((requirement, float(output) == 73.5))
    except ValueError:
        result.append((requirement, False))

    return result
