from wincpy.checks import utils

__winc_id__ = "499e67d5cb54448e93cee7465be2c866"


def check_state(sm):
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

    _, state = utils.execute_module_main(module=sm)
    utils.check_state(expected_state=expected_state, actual_state=state)


def check_output(sm):
    """The output is as expected."""
    output, _ = utils.execute_module_main(module=sm)

    assert (
        float(output.strip()) == 73.5
    ), f"We expected your program's output to be `73.5`, but it was {output}"
