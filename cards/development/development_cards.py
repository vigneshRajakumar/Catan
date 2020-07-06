import abc

class DevelopmentCard(abc.ABC):
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def description(self):
        pass


class Knight(DevelopmentCard):
    def name(self):
        return "Knight"

    def description(self):
        return "lets the player move the robber"

class RoadBuilding(DevelopmentCard):
    def name(self):
        return "Road Building"

    def description(self):
        return "player can place 2 roads as if they just built them"

class YearOfPlenty(DevelopmentCard):
    def name(self):
        return "Year of Plenty"

    def description(self):
        return "the player can draw 2 recource cards of thier chouce from the bank"

class Monopoly(DevelopmentCard):
    def name(self):
        return "Monopoly"

    def description(self):
        return "player can claim all resource cards of a type from other players"

class VictoryPoint(DevelopmentCard):
    def name(self):
        return "Victory Point Card"

    def description(self):
        return "1 additional Vicotry Point"
