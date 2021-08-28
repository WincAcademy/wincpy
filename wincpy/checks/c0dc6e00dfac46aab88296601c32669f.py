""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = ""


def run(student_module):
    result = []

    # Shortification nation
    sm = student_module

    # Probably has all the unique facts :-)
    unique_facts = set([sm.random_koala_fact() for _ in range(5000)])

    requirement = "unique_koala_facts returns koala facts"
    result.append(
        (
            requirement,
            True if set(sm.unique_koala_facts(10)).issubset(unique_facts) else False,
        )
    )

    requirement = "unique_koala_facts returns the right number of facts"
    result.append(
        (
            requirement,
            len(sm.unique_koala_facts(10)) == 10 and
            # There are only 29 facts in the dataset.
            len(sm.unique_koala_facts(50)) == 29,
        )
    )

    requirement = "num_joey_facts returns the right number of joey facts"
    result.append((requirement, sm.num_joey_facts() == 2))

    requirement = "koala_weight returns the right weight"
    result.append((requirement, sm.koala_weight() == 14))

    return result
