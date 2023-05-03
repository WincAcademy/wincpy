from wincpy.checks.utils import StandardChecks

__winc_id__ = "25596924dffe436da9034d43d0af6791"


def check_farm_action(student_module):
    """`farm_action` returns correct values for all test cases"""
    StandardChecks.n_params(student_module.farm_action, n_params=7)
    cases = [
        (
            ("sunny", "day", True, "pasture", "spring", False, True),
            "take cows to cowshed\nmilk cows\ntake cows back to pasture",
        ),
        (("rainy", "night", False, "cowshed", "winter", False, True), "wait"),
        (
            ("rainy", "night", False, "cowshed", "winter", True, True),
            "fertilize pasture",
        ),
        (("windy", "night", True, "cowshed", "winter", True, True), "milk cows"),
        (("bowling", "night", False, "cowshed", "winter", False, True), "wait"),
        (("sunny", "night", True, "cowshed", "summer", False, True), "milk cows"),
        (
            ("rainy", "night", False, "pasture", "winter", False, False),
            "take cows to cowshed",
        ),
    ]

    for args, return_val in cases:
        assert student_module.farm_action(*args) == return_val, (
            "Your implementation did not work when called with these parameters: "
            + "`"
            + str(args)
            + "`"
        )
