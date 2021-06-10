import board

class Battleship:
    def fire(self, p1, p2, i, j):
        """
        p1 fires to p2 at (i, j) -> 0, 0 to 9, 9
        """
        hit_or_miss = p2.update_state(i, j)
        p1.update_fire_logs(hit_or_miss)
        return hit_or_miss

class Player:
    def __init__(self, name):
        self.name = name
        self.board = board.Board(name)
        self.last_input = None
        self.inputs = {}

    def take_input(self):
        """Takes input and fires to opponent."""
        inp = input('Enter input: ')  # F6
        self.last_input = inp
        return ord(inp[0]) - ord('A'), int(inp[1]) - 1  # 4, 5

    def update_state(self, i, j):
        state = self.board.board[i][j]
        if state == board.States.ship:
            self.board.board[i][j] = board.States.hit
            print('it was a hit')
            return board.States.hit
        print('it was a miss')
        return board.States.miss

    def check_all_ships_down(self):
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[0])):
                if self.board.board[i][j] == board.States.ship:
                    return False
        return True

    def update_fire_logs(self, hit_or_miss):
        if self.last_input not in self.inputs:
            self.inputs[self.last_input] = []
        self.inputs[self.last_input].append(hit_or_miss)
