from prettytable import PrettyTable
import random, os

BOARD_SIZE = 4
LEFT = 1
UP = 2
RIGHT = 3
DOWN = 4

class Tile:
    def __init__(self, x, y):
        self.value = 0
        self.moved = False
        self.coords = (x, y)

    def isEmpty(self):
        return self.value == 0

    def add(self, val):
        self.value += val

    def set(self, new):
        self.value = new

    def getCoord(self):
        return self.coords

    def get(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def move_or_merge(self, other):
        if self.value > 0:
            # Move for empty
            if other.isEmpty():
                other.set(self.value)
                self.set(0)
            elif other.get() == self.value:
                other.add(self.value)
                self.set(0)

class Board:
    def __init__(self):
        self.grid = [[Tile(x, y) for y in range(BOARD_SIZE)] for x in range(BOARD_SIZE)]    # x x x x (4 times)

    def generatePiece(self):
        """Generate a 2 or a 4 at a random spot on an empty slot"""

        empty_tiles = []
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.grid[x][y].isEmpty():
                    empty_tiles.append(self.grid[x][y])

        two_or_four = random.choice([2, 4])
        random.choice(empty_tiles).set(two_or_four)

    def print_board(self):
        """Prints the board"""
        ptable = PrettyTable()
        ptable.set_style(12)
        ptable.header = False
        ptable.border = True
        ptable.hrules = 1 # All horizontal rules
        ptable.vrules = 1 # All horizontal rules
        for row in self.grid:
            ptable.add_row(row)
        os.system("clear")
        print("\n \n")
        print(ptable)

    def move(self, move):
        pass

    def right(self, tile):
        x, y = tile.coords
        if x == BOARD_SIZE and y == BOARD_SIZE:
            return None
        elif x == BOARD_SIZE:
            y += 1
            x = 0
        else:
            x += 1

        return self.grid[x][y]
    def left(self, tile):
        x, y = tile.coords
        if x == 0 and y == BOARD_SIZE - 1:
            return None
        elif x == 0:
            y += 1
            x = BOARD_SIZE - 1
        else:
            x -= 1

        return self.grid[x][y]
    def up(self, tile):
        x, y = tile.coords
        if x == BOARD_SIZE and y == BOARD_SIZE:
            return None
        elif x == BOARD_SIZE:
            y += 1
            x = 0
        else:
            x += 1

        return self.grid[x][y]
    def down(self, tile):
        x, y = tile.coords
        if x == BOARD_SIZE and y == BOARD_SIZE:
            return None
        elif x == BOARD_SIZE:
            y += 1
            x = 0
        else:
            x += 1

        return self.grid[x][y]







my_board = Board()
my_board.print_board()
my_board.generatePiece()
my_board.print_board()