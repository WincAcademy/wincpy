import inspect
import re

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "534d85ea1ab14924a91f9eccf6f3f30d"


def run(student_module):
    # Rename for brevity, but keep arg long for readability. You're welcome.
    sm = student_module

    result = []

    main_abspath = get_main_abspath(sm)
    output, state = exec_assignment_code(main_abspath)

    # Do stuff
    requirement = "add() has the correct functionality"
    result.append(
        (
            requirement,
            sm.add(1, 1) == 2
            and sm.add(1.2, 3.8) == 5
            and sm.add("Hi", 2) == 0
            and sm.add(3.2, "Hello") == 0,
        )
    )

    requirement = "add() uses try..except and not if-else"
    src = strip_comments(inspect.getsource(sm.add))
    result.append((requirement, "try" in src and "if" not in src))

    requirement = "read_file() has the correct functionality"
    student_main_src = open(main_abspath).read()
    result.append(
        (
            requirement,
            sm.read_file(main_abspath) == student_main_src
            and sm.read_file("doesnotexist9912.xtx") == "",
        )
    )

    requirement = "read_file() uses try..except and not if-else"
    src = strip_comments(inspect.getsource(sm.read_file))
    result.append((requirement, "try" in src and "if" not in src))

    requirement = "get_item_from_list() has the correct functionality"
    foo = list(range(10))
    result.append(
        (
            requirement,
            sm.get_item_from_list(foo, 9) == 9
            and sm.get_item_from_list(foo, -1) == 9
            and sm.get_item_from_list(foo, 10) is None,
        )
    )

    requirement = "get_item_from_list() uses try..except and not if-else"
    src = strip_comments(inspect.getsource(sm.get_item_from_list))
    result.append((requirement, "try" in src and "if" not in src))

    return result


def strip_comments(src):
    single_line_comment = re.compile(r"#.*\n")
    multiline_comment = re.compile(r'""".*"""')

    cleaned_src = src
    for match in single_line_comment.finditer(src):
        cleaned_src = cleaned_src[: match.start()] + cleaned_src[match.end() :]

    for match in multiline_comment.finditer(src):
        cleaned_src = cleaned_src[: match.start()] + cleaned_src[match.end() :]

    return cleaned_src
