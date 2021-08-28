""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"


# Run tests on given student module.
def run(sm):
    result = []

    requirement = "greet's default case is correct"
    result.append(
        (
            requirement,
            sm.greet("Bob") == "Hello, Bob!" and sm.greet("Alice") == "Hello, Alice!",
        )
    )

    requirement = "greet handles an optional template string correctly"
    result.append(
        (
            requirement,
            sm.greet("Bob", "Testing, <name>!") == "Testing, Bob!"
            and sm.greet("Alice", "Testing, <name>!") == "Testing, Alice!",
        )
    )

    requirement = "force is implemented correctly and uses earth's gravity by default"
    result.append((requirement, sm.force(10) == 98 and round(sm.force(50)) == 490))

    requirement = "force can handle optional body specifications"
    result.append(
        (
            requirement,
            sm.force(10, "sun") == 2740
            and sm.force(10, "pluto") == 6
            and sm.force(10, "saturn") == 104
            and sm.force(10, "earth") == 98,
        )
    )

    requirement = "pull is implemented correctly"
    result.append(
        (
            requirement,
            sm.pull(1, 2, 3) is not None
            and round(sm.pull(800, 1500, 3), 10) == 8.8987e-06,
        )
    )
    result.append(
        (
            requirement,
            sm.pull(1, 2, 3) is not None
            and round(sm.pull(0.1, 5.972 * 10 ** 4, 6.371 * 10 ** 6), 30)
            == 9.819532033e-21,
        )
    )

    return result
