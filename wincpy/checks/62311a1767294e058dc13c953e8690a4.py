from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "62311a1767294e058dc13c953e8690a4"


def run(student_module):
    result = []

    main_abspath = get_main_abspath(student_module)
    output, state = exec_assignment_code(main_abspath)

    # Do stuff
    expected_output = ["Leek is 2 euro per kilo.", "8", "1.6kg broccoli costs 3.74e"]
    for i, line in enumerate(output.split("\n")):
        if line == "":
            continue
        requirement = f"Printed value {i} is correct."
        try:
            result.append((requirement, line == expected_output[i]))
        except:
            result.append((requirement, False))

    return result
