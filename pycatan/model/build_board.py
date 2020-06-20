import random
import tiles

class GameBoard:
    def __init__(self,layout):
        self.layout = layout

    def show_board(self):
        print("  %s %s %s  " % (self.layout[0][0].short_name(), self.layout[0][1].short_name(), self.layout[0][2].short_name()))
        print(" %s %s %s %s " % (self.layout[1][0].short_name(), self.layout[1][1].short_name(), self.layout[1][2].short_name(), self.layout[1][3].short_name()))
        print("%s %s %s %s %s" % (self.layout[2][0].short_name(), self.layout[2][1].short_name(), self.layout[2][2].short_name(), self.layout[2][3].short_name(), self.layout[2][4].short_name()))
        print(" %s %s %s %s " % (self.layout[3][0].short_name(), self.layout[3][1].short_name(), self.layout[3][2].short_name(), self.layout[3][3].short_name()))
        print("  %s %s %s  " % (self.layout[4][0].short_name(), self.layout[4][1].short_name(), self.layout[4][2].short_name()))

def generate_layout():
    layout = []
    tiles = []
    for x in range(4):
        tiles.append(Fields())

    for x in range(4):
        tiles.append(Forest())

    for x in range(4):
        tiles.append(Pasture())

    for x in range(3):
        tiles.append(Hills())

    for x in range(3):
        tiles.append(Mountain())

    tiles.append(Desert())
    random.shuffle(tiles)
    
    layout.append([])
    for x in range(3):
        layout[0].append(tiles.pop())

    layout.append([])
    for x in range(4):
        layout[1].append(tiles.pop())

    layout.append([])
    for x in range(5):
        layout[2].append(tiles.pop())

    layout.append([])
    for x in range(4):
        layout[3].append(tiles.pop())

    layout.append([])
    for x in range(3):
        layout[4].append(tiles.pop())

    return layout

def main():
    layout = generate_layout()
    game_board = GameBoard(layout)
    game_board.show_board()

main()
        
