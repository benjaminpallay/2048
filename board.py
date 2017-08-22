

class Board():


    def __init__(self, board):

        self.board = [[tile for tile in row] for row in board]
        self.size = len(self.board)


    @classmethod
    def empty_board(cls, size):

        board = [[0 for col in range(size)] for row in range(size)]

        return cls(board)


    def __repr__(self):

        string = ""

        for row in self.board:
            line = ""
            for tile in row:
                line += " {0}".format(tile)
            string += "{0}\n".format(line)

        return string


    def rows(self):
        return [row for row in self.board]


    def cols(self):
        return [[row[i] for row in self.rows()] for i in range(len(self.board))]


    def set_tile(self, row, col, value, move=True):

        if move:
            self.board[row][col] = value
        elif not move and not self.board[row][col]:
            self.board[row][col] = value
        else:
            raise ValueError("The tile is not empty")


    def tile_number_to_pos(self, tile_number):

        if tile_number > self.size ** 2 - 1:
            raise ValueError("The tile position doesn't exist")
        else:
            row = tile_number // self.size
            col = tile_number % self.size

            return (row, col)


    def highest_tile_number(self):
        return max([el for row in self.board for el in row])


    def __eq__(self, other):

        if not isinstance(other, Board):
            return False
        else:
            return self.board == other.board and self.size == other.size


    def __hash__(self):

        hash = hash(self.board)

        return 139 * (hash + 139 * self.size)