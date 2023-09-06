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
        "sun": 274,
        "mercury": 3.7,
        "venus": 8.87,
        "earth": 9.798,
        "mars": 3.71,
        "jupiter": 24.92,
        "saturn": 10.44,
        "uranus": 8.87,
        "neptune": 11.15,
        "pluto": 0.58,
        "moon": 1.62
    }

    force = mass * round(bodies[body])
    return force

print(force(10, "pluto"))
# 3


def pull(m1, m2, d):
    G = 6.674 * 10**-11
    return G * ((m1 * m2) / d**2)
