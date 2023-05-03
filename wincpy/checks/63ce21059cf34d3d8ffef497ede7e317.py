from wincpy.checks import utils

__winc_id__ = "63ce21059cf34d3d8ffef497ede7e317"


def check_end_of_line_comments(student_module):
    """Your `main.py` contains two end-of-line comments"""
    src = utils.get_main_src(student_module)
    count = sum([True if l.strip().find("#") > 0 else False for l in src.split("\n")])
    assert (
        count >= 2
    ), f"There should be at least `2` end-of-line comments, but there were only `{count}`"


def check_single_line_comments(student_module):
    """Your `main.py` contains two single-line comments"""
    src = utils.get_main_src(student_module)

    count = sum([True if l.strip().find("#") == 0 else False for l in src.split("\n")])

    assert (
        count >= 4
    ), f"There should be at least `2` single-line comments, but there were only `{count}`"


def check_multiline_comments(student_module):
    """Your `main.py` contains two multi-line comments"""
    src = utils.get_main_src(student_module)
    count = sum(
        [
            True if l.strip() != "" and l.strip()[:3] == '"""' else False
            for l in src.split("\n")
        ]
    )
    assert (
        count >= 2
    ), f"There should be at least `2` multi-line comments, but there were only `{count}`"


def __get_main_src(student_module):
    with open(utils.get_main_abspath(student_module), "r") as f:
        return f.read()
