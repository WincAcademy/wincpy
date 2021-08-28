from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath
import importlib

__winc_id__ = "49bce82ef9cc475ca3146ee15b0259d0"


def run(student_module):
    result = []

    # make it shortah
    sm = student_module

    requirement = "greet() is correct."
    result.append((requirement, sm.greet("Bob") == "Hello, Bob!"))

    requirement = "add() is correct."
    result.append((requirement, sm.add(5, 1, 4) == 10 and sm.add(1, 1, 9) == 11))

    # Try block is for backwards compatibility.
    try:
        requirement = "scottish_greet() is correct."
        result.append(
            (
                requirement,
                sm.scottish_greet("Ian", False) == "Hello, Ian!"
                and sm.scottish_greet("Ian", True) == "Hello, wee Ian!",
            )
        )
    except AttributeError:
        pass

    requirement = "postive() is correct."
    result.append(
        (
            requirement,
            sm.positive(5) is True
            and sm.positive(-5) is False
            and sm.positive(0) is False,
        )
    )

    requirement = "negative() is correct."
    result.append(
        (
            requirement,
            sm.negative(5) is False
            and sm.negative(-5) is True
            and sm.negative(0) is False,
        )
    )

    # Try block is for backwards compatibility.
    try:
        requirement = "sign() is correct."
        result.append(
            (requirement, sm.sign(5) == 1 and sm.sign(-5) == -1 and sm.sign(0) == 0)
        )
    except AttributeError:
        pass

    # Try block is for backwards compatibility.
    try:
        requirement = "nag() is correct."
        result.append(
            (
                requirement,
                sm.nag(1, "ok", 3) is False
                and sm.nag("ok", 2, 3) is False
                and sm.nag("ok", "ok", "wrong") is False
                and sm.nag("Jennie", "bike", 2)
                == "Jennie.. Why can't I have a bike?!\n"
                "Jennie.. Why can't I have a bike?!"
                and sm.nag("Daddy", "Nord Lead 4", 5)
                == "Daddy..... Why can't I have a Nord Lead 4?!\n"
                "Daddy..... Why can't I have a Nord Lead 4?!\n"
                "Daddy..... Why can't I have a Nord Lead 4?!\n"
                "Daddy..... Why can't I have a Nord Lead 4?!\n"
                "Daddy..... Why can't I have a Nord Lead 4?!",
            )
        )
    except AttributeError:
        pass

    return result
