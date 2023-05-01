# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line

# 1


def greet(name, greeting="Hello, <name>!"):
    new_greeting = greeting.replace("<name>", name)
    return new_greeting


# 2


def force(mass, body="earth"):
    bodies = {
        "jupiter": 23.1,
        "neptune": 11.0,
        "saturn": 9.0,
        "earth": 9.8,
        "uranus": 8.7,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.7,
    }

    force = mass * bodies[body]
    return force


print(force(10, "moon"))


# 3


def pull(m1, m2, d):
    G = 6.674 * 10**-11
    return G * ((m1 * m2) / d**2)
