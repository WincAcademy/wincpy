__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

def greet(name, template='Hello, <name>!'):
    return template.replace('<name>', name)


def force(mass, body='earth'):
    gravity_per_body = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.1,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    gravity = gravity_per_body[body]
    return mass * gravity


def pull(m1, m2, d):
    G = 6.674 * 10**-11
    return G * (m1 * m2) / (d ** 2)


if __name__ == '__main__':
    print(greet('Doc'))
    print(greet('Doc', "What's up, <name>!"))

    print(force(10, 'sun'))
    print(force(10, 'pluto'))
    print(force(10, 'saturn'))
    print(force(50, 'earth'))

    # Car example
    print(pull(800, 1500, 3))

    # Earth & an apple
    print(pull(0.1, 5.972 * 10**24, 6.371 * 10**6))
