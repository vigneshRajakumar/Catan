import abc

class Tile(abc.ABC):
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def generate_resource(self):
        pass

    @abc.abstractmethod
    def short_name(self):
        pass

class Forest(Tile):
    def name(self):
        return "Forest"

    def generate_resource(self):
        return "Wood"

    def short_name(self):
        return "fo"

class Pasture(Tile):
    def name(self):
        print("Pasture")

    def generate_resource(self):
        print("Wool")

    def short_name(self):
        return "pa"

class Fields(Tile):
    def name(self):
        return "Fields"

    def generate_resource(self):
        return "Grain" 

    def short_name(self):
        return "fi"

class Hills(Tile):
    def name(self):
        return "Hills"

    def generate_resource(self):
        return "Brick"

    def short_name(self):
        return "hi"

class Mountain(Tile):
    def name(self):
        return "Mountain"

    def generate_resource(self):
        return "Ore" 

    def short_name(self):
        return "mo"

class Desert(Tile):
    def name(self):
        return "Desert"

    def generate_resource(self):
        return "Nothing"

    def short_name(self):
        return "de"
