from wincpy.checks.utils import StandardChecks

__winc_id__ = "f82d22e9845f4b0ea8ff1e3fa6f33a7d"


def check_bouncer_bot(student_module):
    """`bouncer_bot` returns correct values for all test cases"""
    StandardChecks.n_params(student_module.bouncer_bot, n_params=6)
    cases = [
        (
            (False, False, False, False, 17, False),
            "You're too young. Please come back when you're older.",
        ),
        ((False, False, False, True, 25, False), "Please come back when you're sober."),
        (
            (True, False, False, False, 25, False),
            "It's ladies night. Come back another night.",
        ),
        ((False, False, True, False, 25, False), "No, too busy right now."),
        ((False, False, False, False, 25, True), "Welcome!"),
    ]

    for args, return_val in cases:
        assert (
            student_module.bouncer_bot(*args) == return_val
        ), f"When using these parameters: `{str(args)}` The output was not `{return_val}`"
