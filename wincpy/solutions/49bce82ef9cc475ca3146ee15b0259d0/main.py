__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'


def greet(name):
    return f'Hello, {name}!'


def add(a, b, c):
    return a + b + c


def scottish_greet(name, wee):
    if wee:
        return f'Hello, wee {name}!'
    return f'Hello, {name}!'


def positive(x):
    return x > 0


def negative(x):
    return x < 0


def sign(x):
    if type(x) is not int and type(x) is not float:
        return "This doesn't have a sign!"
    if positive(x):
        return 1
    elif negative(x):
        return -1
    return 0


def nag(person, x, repetitions):
    if type(person) is not str:
        return False
    elif type(x) is not str:
        return False
    elif type(repetitions) is not int:
        return False

    dots = '.' * repetitions
    template = f"{person}{dots} Why can't I have a {x}?!\n"
    return (template * repetitions)[:-1]
