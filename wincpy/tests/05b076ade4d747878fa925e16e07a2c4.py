import subprocess

from wincpy.helpers import exec_assignment_code, get_main_abspath

__winc_id__ = '05b076ade4d747878fa925e16e07a2c4'


def run(student_module):
    result = []
    main_abspath = get_main_abspath(student_module)

    output, _ = exec_assignment_code(main_abspath)

    requirement = 'Er wordt iets geprint.'
    result.append((requirement, output != ''))

    return result
