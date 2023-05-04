import inspect
from wincpy.checks import utils
from wincpy.checks.utils import StandardChecks

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"


def check_random_koala_fact(student_module):
    StandardChecks.n_params(student_module.random_koala_fact, n_params=0)

    facts = __get_all_facts(student_module)
    for _ in range(10):
        assert (
            student_module.random_koala_fact() in facts
        ), "`random_koala_fact` returned something other than a koala fact"


def check_unique_koala_fact(student_module):
    StandardChecks.n_params(student_module.unique_koala_facts, n_params=1)

    facts = __get_all_facts(student_module)

    assert (
        len(set(student_module.unique_koala_facts(0))) != 29
    ), "When asking for 0 facts, all the facts are returned"

    for n in range(15):
        assert (
            len(set(student_module.unique_koala_facts(n))) == n
        ), "`unique_koala_facts` returned duplicate koala facts"
        assert set(student_module.unique_koala_facts(n)).issubset(
            facts
        ), "Some of your return values are not koala facts"

    n_unique_facts = 29
    assert (
        len(student_module.unique_koala_facts(50)) == n_unique_facts
    ), "`unique_koala_facts` returned more supposedly unique facts than possible"


def check_num_joey_facts(student_module):
    StandardChecks.n_params(student_module.num_joey_facts, n_params=0)

    assert (
        type(student_module.num_joey_facts()) == int
    ), "`num_joey_facts` returned a `str` but it should be an `int`"
    assert (
        student_module.num_joey_facts() == 2
    ), "`num_joey_facts` did not return the right number"


def check_koala_weight(student_module):
    StandardChecks.n_params(student_module.koala_weight, n_params=0)

    assert (
        student_module.koala_weight() == 14
    ), "`koala_weight` did not return the right number"


def __get_all_facts(student_module):
    # Probably has all the unique facts :-)
    return set([student_module.random_koala_fact() for _ in range(1000)])
