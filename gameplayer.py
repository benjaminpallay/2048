from game import Game


class GamePlayer():


    def __init__(self, strategy, winning_tile, number_of_games):

        self.strategy = strategy
        self.games_won = 0
        self.winning_tile = winning_tile
        self.number_of_games = number_of_games


    def play_game(self):

        game = Game(4)
        game.new_game()

        while not game.game_over():
            # print (game.board)
            valid_move = False
            direction = None
            while not valid_move:
                direction = self.strategy(game)
                if game.allowed_move(direction):
                    valid_move = True
            game.move_board(direction)
            game.new_tiles()
        # print (game.board)

        return game.highest_tile()


    def play_games(self):

        for _ in range(self.number_of_games + 1):
            game_highest_tile = self.play_game()
            if game_highest_tile >= self.winning_tile:
                self.games_won += 1


    def won_games(self):

        self.play_games()

        return self.games_won / self.number_of_games