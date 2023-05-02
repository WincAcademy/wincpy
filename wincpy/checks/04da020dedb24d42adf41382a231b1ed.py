from wincpy.checks.utils import StandardChecks

__winc_id__ = "04da020dedb24d42adf41382a231b1ed"


def check_player_class_init(student_module):
    """The `Player.__init__` method is implemented correctly"""
    StandardChecks.n_params(student_module.Player, n_params=4)

    player = student_module.Player("Super Bob", 0.3, 0.5, 0.5)
    assert player.name == "Super Bob", "player.name is not initialized correctly"
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


def check_player_introduce(student_module):
    """The `Player.introduce` method is implemented correctly"""
    StandardChecks.n_params(student_module.Player, n_params=4)

    player = student_module.Player("Mister Secret Name", 0.3, 0.5, 0.5)
    assert (
        player.introduce() == "Hello everyone, my name is Mister Secret Name."
    ), "Try using an f-string combined with self.name"


def check_player_strength(student_module):
    """The `Player.strength` method is implemented correctly"""
    StandardChecks.n_params(student_module.Player, n_params=4)

    tip = "`.strength()` should return a tuple of the player's best attribute and its value"
    Player = student_module.Player
    assert Player("Super Bob", 0.3, 0.5, 0.5).strength() == ("endurance", 0.5), tip
    assert Player("_ _", 0.3, 0.5, 0.6).strength() == ("accuracy", 0.6), tip
    assert Player("_ _", 0.3, 0.5, 0.6).strength() == ("accuracy", 0.6), tip
    assert Player("_ _", 0.7, 0.5, 0.6).strength() == ("speed", 0.7), tip


def check_commentator_init(student_module):
    """The `Commentator.__init__` method has been implemented correctly"""
    StandardChecks.n_params(student_module.Commentator, n_params=1)

    commentator = student_module.Commentator("Super Double Plus Commentator")
    assert (
        commentator.name == "Super Double Plus Commentator"
    ), "`.name` should be set to the value of the `name` parameter passed to `__init__`"


def check_commentator_sum_player(student_module):
    """The `Commentator.sum_player` method has been implemented correctly"""
    StandardChecks.n_params(student_module.Commentator, n_params=1)
    StandardChecks.n_params(student_module.Commentator.sum_player, n_params=2)

    commentator = student_module.Commentator("Super Double Plus Commentator")
    player = student_module.Player("Super Bob", 0.3, 0.5, 0.5)
    assert (
        commentator.sum_player(player) == 1.3
    ), "`.sum_player()` should return the sum of the player's speed, endurance and accuracy"


def check_commentatory_compare_players(student_module):
    """The `Commentator.compare_players` method has been implemented correctly"""
    StandardChecks.n_params(student_module.Player, n_params=4)
    StandardChecks.n_params(student_module.Commentator, n_params=1)
    StandardChecks.n_params(student_module.Commentator.compare_players, n_params=4)

    commentator = student_module.Commentator("Super Double Plus Commentator")
    alice = student_module.Player("Alice", 0.8, 0.2, 0.6)
    bob = student_module.Player("Bob", 0.5, 0.2, 0.6)
    candice = student_module.Player("Candice", 0.8, 0.2, 0.7)
    dirk = student_module.Player("Dirk", 0.5, 0.2, 0.6)
    eric = student_module.Player("Eric", 0.5, 0.2, 0.6)

    tip = "We compared different players and got a wrong result back"
    assert commentator.compare_players(alice, bob, "speed") == "Alice", tip
    assert commentator.compare_players(alice, candice, "accuracy") == "Candice", tip
    assert (
        commentator.compare_players(dirk, eric, "speed")
        == "These two players might as well be twins!"
    ), tip
