import time
from tictactoe.Tic import Tic
from braco import sr_driver as porta
import random
import cv2
import numpy


def foto2(vet_controle):
    classificador = vet_controle
    print(cv2.__version__)
    camera_porta = 0

    camera = cv2.VideoCapture(camera_porta)
    Arquivo_raiz = "C:/Users/lucas/Desktop/agora vai/imagem.png"
    Arquivo_raiz2 = "C:/Users/lucas/Desktop/agora vai/img2.png"
    Arquivo_teste = "C:/Users/lucas/Desktop/agora vai/part0.png"
    Arquivo_teste1 = "C:/Users/lucas/Desktop/agora vai/part1.png"
    Arquivo_teste2 = "C:/Users/lucas/Desktop/agora vai/part2.png"
    Arquivo_teste3 = "C:/Users/lucas/Desktop/agora vai/part3.png"
    Arquivo_teste4 = "C:/Users/lucas/Desktop/agora vai/part4.png"
    Arquivo_teste5 = "C:/Users/lucas/Desktop/agora vai/part5.png"
    Arquivo_teste6 = "C:/Users/lucas/Desktop/agora vai/part6.png"
    Arquivo_teste7 = "C:/Users/lucas/Desktop/agora vai/part7.png"
    Arquivo_teste8 = "C:/Users/lucas/Desktop/agora vai/part8.png"

    print("tecle ESC para sair ou t para fotografar")

    kernel = numpy.ones((5, 5), numpy.uint8)
    rangomax = numpy.array([235, 75, 75])  # B, G, R
    rangomin = numpy.array([70, 0, 0])
    # -----------------------------------------------------------------------------------------------------------------------
    valor = None
    loop = 0
    while loop == 0:
        retval, img = camera.read(1)
        # cv2.imshow("foto", img)
        k = cv2.waitKey(100)
        if k == 27:
            loop = False
        elif k == ord("t"):
            cv2.imwrite("imagem.png", img)
            loop = False
        if not loop:
            img2 = cv2.imread(Arquivo_raiz)
            mask = cv2.inRange(img2, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(img2, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera', img2)
            cv2.imwrite(Arquivo_raiz2, img2)
        # -----------------------------------------------------------------------------------------------------------------------
        #                                           '''janela 0'''
        if classificador[0] != 0:
            part0 = img[0:160,0:213]
            mask = cv2.inRange(part0, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part0, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part0, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera', part0)
            cv2.imwrite(Arquivo_teste, part0)
            if (at + bt) > 0:
                print("objeto detectado em 0")
                classificador[0] = 0
                # cv2.destroyAllWindows()
                camera.release()
                valor = 0
                break
        # -----------------------------------------------------------------------------------------------------------------------
        #                                              janela 1
        if classificador[1] == 0:
            part1 = img[0:155, 213:426]
            # part0 = cv2.imread("imagem.png")
            mask = cv2.inRange(part1, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part1, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part1, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera1', part1)
            cv2.imwrite(Arquivo_teste1, part1)
            if (at + bt) > 0:
                print("objeto detectado em 1")
                classificador[1] = 1
                # cv2.destroyAllWindows()
                camera.release()
                valor = 1
                break
        # -----------------------------------------------------------------------------------------------------------------------
        #                                               janela 2
        if classificador[2] == 0:
            part2 = img[0:155, 426:640]
            # part0 =cv2.imread("imagem.png")
            mask = cv2.inRange(part2, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part2, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part2, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera2', part2)
            cv2.imwrite(Arquivo_teste2, part2)
            if (at + bt) > 0:
                print("objeto detectado em 2")
                classificador[2] = 2
                # cv2.destroyAllWindows()
                camera.release()
                valor = 2
                break
        # -----------------------------------------------------------------------------------------------------------------------
        #                                             janela 3

        if classificador[3] == 0:
            part3 = img[180:320, 0:213]
            # part0 =cv2.imread("imagem.png")
            mask = cv2.inRange(part3, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part3, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part3, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera3', part3)
            cv2.imwrite(Arquivo_teste3, part3)
            if (at + bt) > 0:
                print("objeto detectado em 3")
                classificador[3] = 3
                # cv2.destroyAllWindows()
                camera.release()
                valor = 3
                break
        # -----------------------------------------------------------------------------------------------------------------------
        #                                            janela 4
        if classificador[4] == 0:
            part4 = img[180:320, 213:426]
            # part0 =cv2.imread("imagem.png")
            mask = cv2.inRange(part4, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part4, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part4, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera4', part4)
            cv2.imwrite(Arquivo_teste4, part4)
            if (at + bt) > 0:
                print("objeto detectado em  4")
                classificador[4] = 4
                # cv2.destroyAllWindows()
                camera.release()
                valor = 4
                break
        # -----------------------------------------------------------------------------------------------------------------------
        #                                             janela 5
        if classificador[5] == 0:
            part5 = img[180:320, 426:640]
            # part0 =cv2.imread("imagem.png")
            mask = cv2.inRange(part5, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part5, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part5, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera5', part5)
            cv2.imwrite(Arquivo_teste5, part5)
            if (at + bt) > 0:
                print("objeto detectado em 5")
                classificador[5] = 5
                # cv2.destroyAllWindows()
                camera.release()
                valor = 5
                break
        # -----------------------------------------------------------------------------------------------------------------------
        #                                   JANELA 6
        if classificador[5] == 0:
            part6 = img[340:480, 0:210]
            # part0 =cv2.imread("imagem.png")
            mask = cv2.inRange(part6, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part6, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part6, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera6', part6)
            cv2.imwrite(Arquivo_teste6, part6)
            if (at + bt) > 0:
                print("objeto detectado em 6")
                classificador[6] = 6
                # cv2.destroyAllWindows()
                camera.release()
                valor = 6
                break
        # -----------------------------------------------------------------------------------------------------------------------
        #                                     JANELA 7
        if classificador[7] == 0:
            part7 = img[340:480, 230:426]
            # part0 =cv2.imread("imagem.png")
            mask = cv2.inRange(part7, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part7, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part7, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera7', part7)
            cv2.imwrite(Arquivo_teste7, part7)
            if (at + bt) > 0:
                print("objeto detectado em 7")
                classificador[7] = 7
                camera.release()
                valor = 7
                break
        # -----------------------------------------------------------------------------------------------------------------------
        #                                    JANELA 8
        if classificador[8] == 0:
            part8 = img[340:480, 440:640]
            # part0 =cv2.imread("imagem.png")
            mask = cv2.inRange(part8, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part8, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part8, (at, bt), 5, (0, 0, 255), -1)
            # cv2.imshow('camera8', part8)
            cv2.imwrite(Arquivo_teste8, part8)
            if (at + bt) > 0:
                print("objeto detectado em 8")
                classificador[8] = 8
                # cv2.destroyAllWindows()
                camera.release()
                valor = 8
                break
        loop += 1
    # -----------------------------------------------------------------------------------------------------------------------
    print(classificador)
    return valor


if __name__ == '__main__':
    def letsPlay():
        board = Tic()
        board.show()
        vet_controle = ["vazio", 0, 0, 0, 0, 0, 0, 0, 0]
        jogadas = 1
        while not board.complete():
            input()
            player = 'X'
            lido = foto2(vet_controle)
            while lido == None:
                lido = foto2(vet_controle)
            player_move = lido
            vet_controle[lido] = lido
            if player_move not in board.available_moves():
                print('Espaço ja ocupado')
                input()
                continue
            board.make_move(player_move, player)
            if board.complete():
                break
            player = board.get_enemy(player)
            computer_move = board.determine(player)
            if random.randint(0, 10) == 5:
                if computer_move + 1 in board.available_moves() and computer_move + 1 < 9:
                    computer_move += 1
                elif computer_move - 1 in board.available_moves() and computer_move - 1 > 0:
                    computer_move -= 1
            moveBraco(computer_move+1, jogadas)
            board.make_move(computer_move, player)
            board.show()
            # time.sleep(2)
            jogadas += 1
        print("winner is", board.winner())
        reacao(board.winner())


    def configSerial():
        nome = 'COM3'
        baud = 19200
        porta.setName(nome)
        porta.setRate(baud)
        porta.inicia()


    def moveBraco(num, mov):
        param_mov = mov * 10
        porta.enviaSerial(param_mov + 2)
        time.sleep(2)
        porta.enviaSerial(param_mov)
        time.sleep(1)
        porta.enviaSerial(param_mov + 1)
        time.sleep(1)
        porta.enviaSerial(14)
        time.sleep(1)
        porta.enviaSerial(param_mov)
        time.sleep(1)
        porta.enviaSerial(param_mov + 2)
        time.sleep(1)
        porta.enviaSerial(0)
        time.sleep(3)
        porta.enviaSerial(num)
        time.sleep(3)
        porta.enviaSerial(13)
        time.sleep(1)
        porta.enviaSerial(60)
        time.sleep(2)
        porta.enviaSerial(0)
        time.sleep(3)

    def reacao(result):
        if result == 'O':
            porta.enviaSerial(62)
        elif result == 'X':
            porta.enviaSerial(61)
        elif result is None:
            porta.enviaSerial(63)




    configSerial()
    letsPlay()
