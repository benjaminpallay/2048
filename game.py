from board import Board


class Game():


    def __init__(self, board_size):

        self.board = Board.empty_board(board_size)
        self.board_size = board_size
        self.score = 0


    def new_game(self):

        self.board = Board.empty_board(self.board_size)
        self.new_tiles(2)
        self.score = 0


    def new_tiles(self, num=1):

        num_tiles = 0

        while num_tiles != num:
            tile = random.choice(range(self.board_size ** 2))
            val = 2 if random.random() > 0.1 else 4
            try:
                position = self.board.tile_number_to_pos(tile)
                self.board.set_tile(position[0], position[1], val, False)
                num_tiles += 1
            except ValueError:
                continue


    def __move(self, line, direction):

        direction = direction.lower()

        pad = lambda new_line: (len(line) - len(new_line)) * [0]
        score = 0
        new_line = line if direction == "r" else line[::-1]

        for i in range(len(new_line) - 1, 0, -1):
            new_line = [l for l in new_line if l]
            new_line = pad(new_line) + new_line
            if new_line[i - 1] == new_line[i]:
                new_line[i] = new_line[i] * 2
                new_line[i - 1] = 0
                score += new_line[i]

        if direction == "l":
            new_line = new_line[::-1]

        return {"score": score, "line": new_line}


    def __transpose_board(self, board):
        return [[col[i] for col in board] for i in
                range(len(board))]


    def move_board(self, direction):

        direction = direction.lower()

        if direction in "ud":
            moved_board_info = [
                self.__move(col, "r") if direction == "d"
                else self.__move(col, "l") for col in self.board.cols()]
        else:
            moved_board_info = [self.__move(row, direction) for row
                                in self.board.rows()]

        score = sum([_["score"] for _ in moved_board_info])
        new_board = [_["line"] for _ in moved_board_info]
        new_board = self.__transpose_board(
            new_board) if direction in "ud" else new_board
        self.board = Board(new_board)
        self.score += score


    def allowed_move(self, direction):

        direction = direction.lower()
        original_board = Board(self.board.board)
        self.move_board(direction)
        allowed = True if self.board != original_board else False
        self.board = Board(original_board.board)

        return allowed


    def game_over(self):
        return len([dir for dir in "ldur" if self.allowed_move(dir)]) == 0


    def highest_tile(self):
        return self.board.highest_tile_number()