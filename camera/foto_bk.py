import cv2
import numpy

def foto2():
    vet_analise = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    camera_porta = 0
    camera = cv2.VideoCapture(0)
    Arquivo_raiz = "imagem.png"

    print("tecle ESC para sair ou t para fotografar")

    kernel = numpy.ones((5, 5), numpy.uint8)
    rangomax = numpy.array([255, 55, 55])  # B, G, R
    rangomin = numpy.array([51, 0, 0])
    # -----------------------------------------------------------------------------------------------------------------------
    loop = 0
    while loop < 7:
        retval, img = camera.read(0)
        cv2.imshow("foto", img)
        cv2.imwrite(Arquivo_raiz, img)
        # -----------------------------------------------------------------------------------------------------------------------
        #                                           '''janela 0'''
        if vet_analise[0] == 0:
            part0 = img[0:155, 0:213]
            mask = cv2.inRange(part0, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part0, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part0, (at, bt), 5, (0, 0, 255), -1)
            cv2.imshow('camera', part0)
            print("jogada na casa 0")
            if (at + bt) > 0:
                vet_analise[0] = 1
                print("objeto detectado")
        # -----------------------------------------------------------------------------------------------------------------------
        #                                              janela 1
        if vet_analise[1] == 0:
            part1 = img[0:155, 213:426]
            mask = cv2.inRange(part1, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part1, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part1, (at, bt), 5, (0, 0, 255), -1)
            cv2.imshow('camera1', part1)
            print("jogada na casa 1")
            if (at + bt) > 0:
                vet_analise[1] = 1
                print("objeto detectado em 1")
        # -----------------------------------------------------------------------------------------------------------------------
        #                                               janela 2
        if vet_analise[2] == 0:
            part2 = img[0:155, 426:640]
            mask = cv2.inRange(part2, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part2, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part2, (at, bt), 5, (0, 0, 255), -1)
            cv2.imshow('camera2', part2)
            print("jogada na casa 2")
            if (at + bt) > 0:
                vet_analise[2] = 1
                print("objeto detectado em 2")
        # -----------------------------------------------------------------------------------------------------------------------
        #                                             janela 3

        if vet_analise[3] == 0:
            part3 = img[160:320, 0:213]
            mask = cv2.inRange(part3, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part3, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part3, (at, bt), 5, (0, 0, 255), -1)
            cv2.imshow('camera3', part3)
            print("jogada na casa 3")
            if (at + bt) > 0:
                vet_analise[3] = 1
                print("objeto detectado em 3")
        # -----------------------------------------------------------------------------------------------------------------------
        #                                            janela 4
        if vet_analise[4] == 0:
            part4 = img[160:320, 213:426]
            mask = cv2.inRange(part4, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part4, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part4, (at, bt), 5, (0, 0, 255), -1)
            cv2.imshow('camera4', part4)
            print("jogada na casa 4")
            if (at + bt) > 0:
                vet_analise[4] = 1
                print("objeto detectado em  4")
        # -----------------------------------------------------------------------------------------------------------------------
        #                                             janela 5
        if vet_analise[5] == 0:
            part5 = img[160:320, 426:640]
            mask = cv2.inRange(part5, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part5, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part5, (at, bt), 5, (0, 0, 255), -1)
            cv2.imshow('camera5', part5)
            print("jogada na casa 5")
            if (at + bt) > 0:
                vet_analise[5] = 1
                print("objeto detectado em 5")
        # -----------------------------------------------------------------------------------------------------------------------
        #                                   JANELA 6
        if vet_analise[5] == 0:
            part6 = img[320:480, 0:210]
            mask = cv2.inRange(part6, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part6, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part6, (at, bt), 5, (0, 0, 255), -1)
            cv2.imshow('camera6', part6)
            print("jogada na casa 6")
            if (at + bt) > 0:
                vet_analise[6] = 1
                print("objeto detectado em 6")
        # -----------------------------------------------------------------------------------------------------------------------
        #                                     JANELA 7
        if vet_analise[7] == 0:
            part7 = img[320:480, 213:426]
            mask = cv2.inRange(part7, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part7, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part7, (at, bt), 5, (0, 0, 255), -1)
            cv2.imshow('camera7', part7)
            print("jogada na casa 7")
            if (at + bt) > 0:
                vet_analise[7] = 1
                print("objeto detectado em 7")
        # -----------------------------------------------------------------------------------------------------------------------
        #                                    JANELA 8
        if vet_analise[8] == 0:
            part8 = img[320:480, 426:640]
            mask = cv2.inRange(part8, rangomin, rangomax)
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            x, y, w, h = cv2.boundingRect(opening)
            at = int(x + w / 2)
            bt = int(y + h / 2)
            cv2.rectangle(part8, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(part8, (at, bt), 5, (0, 0, 255), -1)
            cv2.imshow('camera8', part8)
            print("jogada na casa 8")
            if (at + bt) > 0:
                vet_analise[8] = 1
                print("objeto detectado em 8")
        loop += 1
    # -----------------------------------------------------------------------------------------------------------------------
    cv2.destroyAllWindows()
    camera.release()
    print(vet_analise)
    return vet_analise

foto2()

'''vet_lido = foto2()
for esp in range(len(vet_controle)):
    global vet_controle
    global vet_lido
    if vet_controle[esp] != vet_lido[esp]:
        vet_controle[esp] = vet_lido[esp]
        print('Nova jogada na posição {}'.format(esp))
        print(foto2())'''
