# PART 1


def greet(name, template='Hello, <name>!'):
    return template.replace('<name>', name)


print(greet('Doc'))
print(greet('Doc', "What's up, <name>!"))


# PART 2

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


# Car example
print(pull(800, 1500, 3))

# Earth & an apple
print(pull(0.1, 5.972 * 10**24, 6.371 * 10**6))
