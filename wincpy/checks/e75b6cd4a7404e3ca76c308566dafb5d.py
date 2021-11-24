from wincpy.checks import utils

__winc_id__ = "e75b6cd4a7404e3ca76c308566dafb5d"


def check_output(student_module):
    """All output is as expected."""
    output, _ = utils.exec_main(student_module)
    assert output == "Hello, world", (
        f"Expected output\n\n`'Hello, world'`\n\nbut it was\n\n`'{output}'`\n\n"
        + " (empty)"
        if not output
        else ""
    )
