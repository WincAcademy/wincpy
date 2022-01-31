import inspect
import re

from wincpy.checks import utils
from wincpy.checks.utils import StandardChecks

__winc_id__ = "534d85ea1ab14924a91f9eccf6f3f30d"


def check_add(student_module):
    StandardChecks.n_params(student_module.add, n_params=2)

    assert student_module.add(1, 1) == 2, "`1+1` should be 2"
    assert student_module.add(1.2, 3.8) == 5, "`1.2 + 3.8` should be 5"
    assert student_module.add("Hi", 2) == 0, "'Hi' + 2 should return `0`"
    assert student_module.add(3.2, "Hello") == 0, "`3.2 + 'Hello' should return `0`"

    src = strip_comments(inspect.getsource(student_module.add))
    assert (
        "try" in src and "if" not in src
    ), "`add` should make use of `try..except` and not `if`"


def check_read_file(student_module):
    StandardChecks.n_params(student_module.read_file, n_params=1)

    main_abspath = utils.get_main_abspath(student_module)
    with open(main_abspath, "r") as f:
        main_src = f.read()
    assert (
        student_module.read_file(main_abspath) == main_src
    ), "`read_file` doesn't read files correctly"

    assert (
        student_module.read_file("doesnotexist9912.xtx") == ""
    ), "`read_file` doesn't handle files that don't exist correctly"

    src = strip_comments(inspect.getsource(student_module.read_file))
    assert (
        "try" in src and "if" not in src
    ), "`read_file` should make use of `try..except` and not `if`"


def check_get_item_from_list(student_module):
    StandardChecks.n_params(student_module.get_item_from_list, n_params=2)

    foo = list(range(10))
    assert student_module.get_item_from_list(foo, 9) == 9
    assert student_module.get_item_from_list(foo, -1) == 9
    assert student_module.get_item_from_list(foo, 10) is None

    src = strip_comments(inspect.getsource(student_module.get_item_from_list))
    assert (
        "try" in src and "if" not in src
    ), "`get_item_from_list` should make use of `try..except` and not `if`"


def strip_comments(src):
    single_line_comment = re.compile(r"#.*\n")
    multiline_comment = re.compile(r'""".*"""')

    cleaned_src = src
    for match in single_line_comment.finditer(src):
        cleaned_src = cleaned_src[: match.start()] + cleaned_src[match.end() :]

    for match in multiline_comment.finditer(src):
        cleaned_src = cleaned_src[: match.start()] + cleaned_src[match.end() :]

    return cleaned_src
