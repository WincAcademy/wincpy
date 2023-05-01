from wincpy.checks import utils

__winc_id__ = "499e67d5cb54448e93cee7465be2c866"


def check_state(student_module):
    """All variables are named, filled in and computed correctly."""
    expected_state = {
        "broccoli": 2,
        "leek": 2,
        "potato": 3,
        "brussel_sprout": 7,
        "sum_one_each": 14,
        "avg_price": 3.5,
        "num_broccolis": 5,
        "num_leeks": 2,
        "num_potatoes": 7,
        "num_brussel_sprouts": 10,
        "sum_total": 105,
        "discount_percentage": 30,
        "discounted_sum_total": 73.5,
    }

    _, state = utils.exec_main(student_module)
    utils.check_state(expected_state=expected_state, actual_state=state)


def check_output(student_module):
    """The output is as expected."""
    output, _ = utils.exec_main(student_module)
    split_output = output.split("\n")
    last_print = split_output[-1]
    assert (
        float(last_print) == 73.5
    ), f"We expected your program's last print to be `73.5`, but it was `{last_print}`"
