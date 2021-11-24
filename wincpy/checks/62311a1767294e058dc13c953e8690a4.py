from wincpy.checks import utils

__winc_id__ = "62311a1767294e058dc13c953e8690a4"


def check_output(student_module):
    """All the output is correct, and in the right order."""
    output, _ = utils.exec_main(student_module)
    expected_output = ["Leek is 2 euro per kilo.", "8", "1.6kg broccoli costs 3.74e"]
    for i, line in enumerate(output.split("\n")):
        if i >= len(expected_output):
            raise AssertionError("There were more lines of output than expected")
        if line == "":
            pass
        assert (
            line == expected_output[i]
        ), f"Expected line **{i}** to be\n\n`{expected_output[i]}`\n\nbut it was \n\n`{line}`"
