""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "e75b6cd4a7404e3ca76c308566dafb5d"


def run(student_module):
    result = []

    main_abspath = get_main_abspath(student_module)
    output, state = exec_assignment_code(main_abspath)

    result.append(("Hello world is printed.", output == "Hello world\n"))

    return result
