# Don't change this
__winc_id__ = '9920545368b24a06babf1b57cee44171'
__human_name__ = 'refactoring'

# Your code below this line.
class Specialist():
    def __init__(self, name):
        self.name = name


class Electrician(Specialist):
    pass


class Painter(Specialist):
    pass


class Plumber(Specialist):
    pass


class Homeowner():
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs
        self.contracts = []

    def add_contract(self, specialist):
        self.contracts.append(specialist)


# Classes are hashable so they can be used as keys in dictionaries
specialists = {
    Electrician: Electrician('Alice Aliceville'),
    Painter: Painter('Bob Bobsville'),
    Plumber: Plumber('Craig Craigsville')
}

homeowners = [
    Homeowner('Alfred Alfredson', 'Alfredslane 123', [Painter, Plumber]),
    Homeowner('Bert Bertson', 'Bertslane 231', [Plumber]),
    Homeowner('Candice Candicedottir', 'Candicelane 312', [Electrician, Painter])
]

for homeowner in homeowners:
    for need in homeowner.needs:
        homeowner.add_contract(specialists[need])
    print(f"{homeowner.name}'s contracts:",
          [specialist.name for specialist in homeowner.contracts])
