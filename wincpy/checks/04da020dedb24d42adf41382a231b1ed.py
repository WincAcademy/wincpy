""" template.py

Template for writing tests. This is just a file for convenience and has no
importance beyond it."""

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "04da020dedb24d42adf41382a231b1ed"


def check_player_class_init(student_module):
    """The `Player.__init__` method is implemented correctly"""
    player = student_module.Player("Super Bob", 0.3, 0.5, 0.5)
    assert player.name == "Super Bob", "player.name is initialized correctly"
    assert player.speed == 0.3
    assert player.endurance == 0.5
    assert player.accuracy == 0.5
    try:
        student_module.Player("Bob", -2, 5, 9)
        raise Exception(
            "The Player class init function doesn't handle erroneous values correctly."
        )
    except ValueError:
        # Expected behavior
        pass


def rrun(student_module):
    result = []

    """ Part 1 """
    requirement = "Player class init is implemented correctly"
    player = student_module.Player("Super Bob", 0.3, 0.5, 0.5)
    result.append(
        (
            requirement,
            player.name == "Super Bob"
            and player.speed == 0.3
            and player.endurance == 0.5
            and player.accuracy == 0.5,
        )
    )

    requirement = "Player class init function handles erroneous values correctly"
    try:
        student_module.Player("Bob", -2, 5, 9)
        result.append((requirement, False))
    except ValueError:
        result.append((requirement, True))

    requirement = "Player.introduce() is implemented correctly"
    result.append(
        (requirement, player.introduce() == "Hello everyone, my name is Super Bob.")
    )

    requirement = "Player.strength() is implemented correctly"
    result.append((requirement, player.strength() == ("endurance", 0.5)))

    """ Part 2 """
    requirement = "Commentator class initialization is implemented correctly"
    commentator = student_module.Commentator("Super Double Plus Commentator")
    result.append((requirement, commentator.name == "Super Double Plus Commentator"))

    requirement = "Commentator.sum_player() is implemented correctly"
    result.append((requirement, commentator.sum_player(player) == 1.3))

    requirement = "Commentator.compare_players() is implemented correctly"
    alice = student_module.Player("Alice", 0.8, 0.2, 0.6)
    bob = student_module.Player("Bob", 0.5, 0.2, 0.6)
    candice = student_module.Player("Candice", 0.8, 0.2, 0.7)
    dirk = student_module.Player("Dirk", 0.5, 0.2, 0.6)
    eric = student_module.Player("Eric", 0.5, 0.2, 0.6)

    result.append(
        (
            requirement,
            commentator.compare_players(alice, bob, "speed") == "Alice"
            and commentator.compare_players(alice, candice, "accuracy") == "Candice"
            and commentator.compare_players(dirk, eric, "speed")
            == "These two players might as well be twins!",
        )
    )

    return result
