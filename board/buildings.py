import abc

class Building(abc.ABC):
    
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name

    def description(self):
        return "%s owned by %s" % (self.name, self.owner)

class Abode(Building):
    def __init__(self, owner, name, victory_points):
        super.__init__(owner, name)
        self.victory_points = victory_points

class Settlement(Abode):
    def __init__(self, owner):
        super.__init__(self, owner, "Settlement", 1)

class City(Abode):
    def __init__(self, owner):
        super.__init__(self, owner, "City", 2)

class Road(Building):
    def __init__(self, owner):
        super.__init__(self, owner, "Road")

class Point:
    def __init__(self, abode, position, n1, n2, n3):
        self.abode = abode
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3