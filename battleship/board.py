import enum

class States(enum.Enum):
    empty = 0
    ship = 1
    hit = 2
    miss = 3

class Board:
    def __init__(self, name):
        """Initalitilises random board."""
        self.board = [[States.empty] * 10 for _ in range(10)]
        if name == 'p1':
            self.board[0][4] = States.ship
            self.board[0][5] = States.ship
            self.board[0][6] = States.ship
        else:
            
            self.board[1][4] = States.ship
            self.board[1][5] = States.ship
            self.board[1][6] = States.ship
