from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = '7152c06aa3ac4d5f964ca8619ecb7e8f'


def run(student_module):
    result = []
    main_abspath = get_main_abspath(student_module)

    _, assignment_state = exec_assignment_code(main_abspath)
    types_in_state = [type(var) for var in assignment_state.values()]

    requirement = 'Er wordt een bool gedeclareerd.'
    result.append((requirement, bool in types_in_state))

    requirement = 'Er wordt een string gedeclareerd.'
    result.append((requirement, str in types_in_state))

    requirement = 'Er wordt een int gedeclareerd.'
    result.append((requirement, int in types_in_state))

    return result
