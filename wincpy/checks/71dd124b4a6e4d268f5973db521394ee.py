from wincpy.checks import utils

__winc_id__ = "71dd124b4a6e4d268f5973db521394ee"


def check_state(student_module):
    """All the variables are named and filled in as expected"""
    _, state = utils.exec_main(student_module)
    expected_state = {
        "goal_0": 32,
        "goal_1": 54,
        "scorers": "Ruud Gullit 32, Marco van Basten 54",
        "report": "Ruud Gullit scored in the 32nd minute\n"
        + "Marco van Basten scored in the 54th minute",
    }
    utils.check_state(expected_state, state)

    player = state.get("player", None)
    assert player, "There is no variable `player` declared in your code"
    assert (
        type(player) is str
    ), f"Expected `player` to contain a `str` but it contained a {type(player)}"

    expected_state = {
        "first_name": player[: player.find(" ")],
        "last_name_len": len(player[player.find(" ") + 1 :]),
        "name_short": player[0] + "." + player[player.find(" ") :],
        "chant": (
            (player[: player.find(" ")] + "! ") * len(player[: player.find(" ")])
        )[:-1],
        "good_chant": True,
    }
    utils.check_state(expected_state, state)
