from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = '7152c06aa3ac4d5f964ca8619ecb7e8f'


def run(student_module):
    result = []
    main_abspath = get_main_abspath(student_module)

    _, assignment_state = exec_assignment_code(main_abspath)
    types_in_state = [type(var) for var in assignment_state.values()]

    requirement = "There's a bool in your code."
    result.append((requirement, bool in types_in_state))

    requirement = "There's a string in your code."
    result.append((requirement, str in types_in_state))

    requirement = "There's an int in your code."
    result.append((requirement, int in types_in_state))

    return result
