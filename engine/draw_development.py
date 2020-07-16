import abc
import random

def build_deck():
    deck = []
    for x in range(14):
        deck.append(Knight())
    for x in range(5):
        deck.append(VictoryPoint())
    for x in range(2):
        deck.append(RoadBuilding())
        deck.append(YearOfPlenty())
        deck.append(Monopoly())
    return deck

def main():
    deck = build_deck()
    random.shuffle(deck)

    for card in deck:
        input("Press Enter to draw a card. . .")
        print(card.name())
        print(card.description())

main()

