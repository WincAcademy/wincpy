from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = '7599944cfbd94b47beffdbab7a208931'


def run(student_module):
    result = []
    main_abspath = get_main_abspath(student_module)

    output, state = exec_assignment_code(main_abspath)

    requirement = 'one is True'
    result.append((requirement, state['one'] is True))

    requirement = 'two is True'
    result.append((requirement, state['two'] is True))

    requirement = 'three is True'
    result.append((requirement, state['three'] is True))

    return result
