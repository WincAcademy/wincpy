__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'


class Player():
    def __init__(self, name, speed, endurance, accuracy):
        for x in [speed, endurance, accuracy]:
            if x > 1 or x < 0:
                raise ValueError('Speed, endurance and accuracy must be in range [0, 1]')

        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f'Hello everyone, my name is {self.name}.'

    def strength(self):
        best = (None, -1)
        for attr in ['speed', 'endurance', 'accuracy']:
            value = getattr(self, attr)
            if value > best[1]:
                best = (attr, value)
        return best


class Commentator():
    def __init__(self, name):
        self.name = name

    def sum_player(self, p):
        # We received 'self' here even though we are not using it
        return sum([getattr(p, 'speed'), getattr(p, 'endurance'), getattr(p, 'accuracy')])

    def compare_players(self, p1, p2, attr):
        p1_attr = getattr(p1, attr)
        p2_attr = getattr(p1, attr)

        # First comparison
        if p1_attr > p2_attr:
            return p1.name
        elif p2_attr > p1_attr:
            return p2.name

        # Second case
        p1_strength = p1.strength()[1]
        p2_strength = p2.strength()[1]
        if p1_strength > p2_strength:
            return p1.name
        elif p2_strength > p1_strength:
            return p2.name

        # Third case
        if self.sum_player(p1) > self.sum_player(p2):
            return p1.name
        elif self.sum_player(p2) > self.sum_player(p1):
            return p2.name

        # Finally..
        return 'These two players might as well be twins!'


if __name__ == '__main__':
    alice = Player('Alice', 0.8, 0.2, 0.6)
    bob = Player('Bob', 0.5, 0.2, 0.6)
    candice = Player('Candice', 0.8, 0.2, 0.7)
    dirk = Player('Dirk', 0.5, 0.2, 0.6)
    eric = Player('Eric', 0.5, 0.2, 0.6)

    print(alice.strength())
    print(bob.introduce())

    ray = Commentator('Ray')

    # Winner: Alice
    print(ray.compare_players(alice, bob, 'speed'))

    # Winner: Candice
    print(ray.compare_players(alice, candice, 'accuracy'))

    # Winner: twins!
    print(ray.compare_players(dirk, eric, 'speed'))
