from tictactoe.Tic import Tic

if __name__ == "__main__":
    board = Tic()

    while not board.complete():
        player = 'X'
        player_move = int(input("Next Move: ")) - 1
        if player_move not in board.available_moves():
            continue
        board.make_move(player_move, player)
        board.show()
        if board.complete():
            break
        player = board.get_enemy(player)
        computer_move = board.determine(player)
        board.make_move(computer_move, player)

        board.show()
    print("winner is", board.winner())
