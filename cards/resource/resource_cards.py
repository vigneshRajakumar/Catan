import abc

class ResourceCard(abc.ABC):
    @abc.abstractmethod
    def name(self):
        pass

class Wood(ResourceCard):
    def name(self):
        return "Wood"

class Wool(ResourceCard):
    def name(self):
        return "Wool"

class Grain(ResourceCard):
    def name(self):
        return "Grain"

class Brick(ResourceCard):
    def name(self):
        return "Brick"

class Ore(ResourceCard):
    def name(self):
        return "Ore"