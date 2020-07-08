import abc

class Building(abc.ABC):
    
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name

    def description(self):
        return "%s owned by %s" % (self.name, self.owner)

class Abode(Building):
    def __init__(self, owner, name, point, victory_points):
        super.__init__(owner, name)
        self.point = point
        self.victory_points = victory_points

class Settlement(Abode):
    def __init__(self, owner, point):
        super.__init__(self, owner, "Settlement", point, 1)

class City(Abode):
    def __init__(self, owner, point):
        super.__init__(self, owner, "City", point, 2)

class Road(Building):
    def __init__(self, owner, edge):
        super.__init__(self, owner, "Road")
        self.edge = edge