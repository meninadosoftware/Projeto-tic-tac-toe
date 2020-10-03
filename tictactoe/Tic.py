import random

class Tic:
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self, squares=[]):
        if len(squares) == 0:
            self.squares = [None for i in range(9)]
        else:
            self.squares = squares

    def show(self):
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print(element)

    def available_moves(self):
        """what spots are left empty?"""
        return [k for k, v in enumerate(self.squares) if v is None]

    def available_combos(self, player):
        """what combos are available?"""
        return self.available_moves() + self.get_squares(player)

    def complete(self):
        """is the game over?"""
        if None not in [v for v in self.squares]:
            return True
        if self.winner() is not None:
            return True
        return False

    def x_won(self):
        return self.winner() == 'X'

    def o_won(self):
        return self.winner() == 'O'

    def tied(self):
        return self.complete() == True and self.winner() is None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_squares(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def get_squares(self, player):
        """squares that belong to a player"""
        return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self, position, player):
        """place on square on the board"""
        self.squares[position] = player

    @staticmethod
    def get_enemy(player):
        if player == 'X':
            return 'O'
        return 'X'

    def determine(self, player):
        a = -2
        choices = []
        if len(self.available_moves()) == 9:
            return 4
        for move in self.available_moves():
            self.make_move(move, player)
            val = self.alphabeta(self, self.get_enemy(player), -2, 2)
            self.make_move(move, None)
            # print("move:", move + 1, "causes:", self.winners[val + 1])
            if val > a:
                a = val
                choices = [move]
            elif val == a:
                choices.append(move)
        return random.choice(choices)

    def alphabeta(self, node, player, alpha, beta):
        if node.complete():
            if node.x_won():
                return -1
            elif node.tied():
                return 0
            elif node.o_won():
                return 1
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, Tic().get_enemy(player), alpha, beta)
            node.make_move(move, None)
            if player == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == 'O':
            return alpha
        else:
            return beta
