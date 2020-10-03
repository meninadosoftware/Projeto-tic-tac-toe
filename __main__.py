import time
from tictactoe.Tic import Tic
from camera import identificador as lt_camera
from braco import sr_driver as porta
import random

if __name__ == '__main__':
    def letsPlay():
        board = Tic()
        board.show()
        vet_controle = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        jogadas = 1
        while not board.complete():
            player = 'X'
            lido = lt_camera.foto2(vet_controle)
            player_move = lido
            vet_controle[lido] = lido
            if player_move not in board.available_moves():
                continue
            board.make_move(player_move, player)
            board.show()
            if board.complete():
                break
            player = board.get_enemy(player)
            computer_move = board.determine(player)
            if random.randint(0, 2) == 1:
                computer_move += 1
            moveBraco(computer_move+1, jogadas)
            board.make_move(computer_move, player)
            board.show()
            time.sleep(2)
            jogadas += 1
        print("winner is", board.winner())
    '''def configSerial():
        nome = 'COM3'
        baud = 115200
        porta.setName(nome)
        porta.setRate(baud)
        porta.inicia()'''
    def moveBraco(num, mov):
        def pegarPeca(mov):
            param_mov = mov * 10
            porta.enviaSerial(param_mov)
            porta.enviaSerial(param_mov+1)
            porta.enviaSerial(99)
            porta.enviaSerial(param_mov+2)
            porta.enviaSerial(0)
        porta.enviaSerial(0)
        # pegarPeca(mov)
        porta.enviaSerial(num)
        porta.enviaSerial(101)
        porta.enviaSerial(0)

    #configSerial()
    #letsPlay()
