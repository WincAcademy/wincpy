__winc_id__ = "6eb355e1a60f48a28a0bbbd0c88d9ab4"


def check_alphabetical_order(student_module):
    assert student_module.alphabetical_order(["b", "a", "c"]) == ["a", "b", "c"]
    assert student_module.alphabetical_order(["b", "c", "d"]) == ["b", "c", "d"]
    assert student_module.alphabetical_order([5, 1, 5]) == [1, 5, 5]


def check_won_golden_globe(student_module):
    assert student_module.won_golden_globe("Jeff") is False
    assert student_module.won_golden_globe("jaws") is True
    assert student_module.won_golden_globe("JAWS") is True
    assert student_module.won_golden_globe("memoirs of a geisha") is True
    assert student_module.won_golden_globe("test") is False


def check_remove_toto_albums(student_module):
    assert student_module.remove_toto_albums(["Old Is New"]) == []
    assert student_module.remove_toto_albums([]) == []
    assert student_module.remove_toto_albums(["test", "Old Is New"]) == ["test"]
    assert student_module.remove_toto_albums(["test", "Fahrenheit", "Old Is New"]) == [
        "test"
    ]
