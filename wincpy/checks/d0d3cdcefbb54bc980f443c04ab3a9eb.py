""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "d0d3cdcefbb54bc980f443c04ab3a9eb"


def run(student_module):
    result = []

    main_abspath = get_main_abspath(student_module)
    output, state = exec_assignment_code(main_abspath)

    expected_evals = [False, True, True, False, True, True, True]
    # TODO (not urgent, improvement): check if the correct operators have been
    # used in addition to just checking the result.
    for i, line in enumerate(output.split("\n")):
        if line == "":
            continue
        requirement = f"Evaluation {i+1} is correct."
        try:
            result.append((requirement, line == str(expected_evals[i])))
        except IndexError:
            result.append(("You printed more values than we expected.", False))

    return result
