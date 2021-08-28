""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "05b076ade4d747878fa925e16e07a2c4"


def run(student_module):
    result = []

    main_abspath = get_main_abspath(student_module)
    output, state = exec_assignment_code(main_abspath)

    result.append(("Something is printed.", output != ""))

    return result
