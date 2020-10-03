import cv2
import time
import numpy

vet_leitura=[0,0,0,0,0,0,0,0,0]
def visao3(vet_leitura):
    frame = cv2.VideoCapture(1)
    kernel = numpy.ones((5, 5), numpy.uint8)
    rangomax = numpy.array([255, 55, 55])  # B, G, R
    rangomin = numpy.array([51, 0, 0])
    while True:
            #----------------------------------------------------------------------------------------------------------------------------
        '''janela 0'''
        frame0 = frame[0:155, 0:213]#primei vem o exixo y depois o x
        mask = cv2.inRange(frame0, rangomin, rangomax)
        # reduce the noise
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        x, y, w, h = cv2.boundingRect(opening)
        at = int(x + w / 2)
        bt = int(y + h / 2)
        cv2.rectangle(frame0, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame0, (at, bt), 5, (0, 0, 255), -1)
        cv2.imshow(" imagem 1", frame0 )#cria a janela para visualizaçao

    #----------------------------------------------------------------------------------------------------------------------------
        '''janela 1'''
        frame1 = frame[0:155, 213:426]#primei vem o exixo y depois o x
        mask = cv2.inRange(frame, rangomin, rangomax)
        # reduce the noise
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        x, y, w, h = cv2.boundingRect(opening)
        at = int(x + w / 2)
        bt = int(y + h / 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame, (at, bt), 5, (0, 0, 255), -1)
        cv2.imshow(" imagem 2", frame1)

    #----------------------------------------------------------------------------------------------------------------------------
        '''janela 2'''
        frame2 = frame[0:155, 426:640]#primei vem o exixo y depois o x
        mask = cv2.inRange(frame2, rangomin, rangomax)
        # reduce the noise
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        x, y, w, h = cv2.boundingRect(opening)
        at = int(x + w / 2)
        bt = int(y + h / 2)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame2, (at, bt), 5, (0, 0, 255), -1)
        cv2.imshow("imagem3", frame2)

    #----------------------------------------------------------------------------------------------------------------------------
        '''janela 3'''
        frame3 = frame[160:320, 0:213]#primei vem o exixo y depois o x
        mask = cv2.inRange(frame3, rangomin, rangomax)
        # reduce the noise
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        x, y, w, h = cv2.boundingRect(opening)
        at = int(x + w / 2)
        bt = int(y + h / 2)
        cv2.rectangle(frame3, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame3, (at, bt), 5, (0, 0, 255), -1)
        cv2.imshow("imagem 4", frame3)

    #----------------------------------------------------------------------------------------------------------------------------
        '''janela 4'''
        frame4 = frame[160:320, 213:426]#primei vem o exixo y depois o x
        mask = cv2.inRange(frame4, rangomin, rangomax)
        # reduce the noise
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        x, y, w, h = cv2.boundingRect(opening)
        at = int(x + w / 2)
        bt = int(y + h / 2)
        cv2.rectangle(frame4, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame4, (at, bt), 5, (0, 0, 255), -1)
        cv2.imshow("imagem 5", frame4)

    #----------------------------------------------------------------------------------------------------------------------------
        '''janela 5'''
        frame5 = frame[160:320, 426:640]#primei vem o exixo y depois o x
        mask = cv2.inRange(frame0, rangomin, rangomax)
        # reduce the noise
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        x, y, w, h = cv2.boundingRect(opening)
        at = int(x + w / 2)
        bt = int(y + h / 2)
        cv2.rectangle(frame5, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame5, (at, bt), 5, (0, 0, 255), -1)
        cv2.imshow("imagem 6", frame5)

    #----------------------------------------------------------------------------------------------------------------------------
        '''janela 6'''
        frame6 = frame[320:480, 0:210]#primei vem o exixo y depois o x
        mask = cv2.inRange(frame6, rangomin, rangomax)
        # reduce the noise
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        x, y, w, h = cv2.boundingRect(opening)
        at = int(x + w / 2)
        bt = int(y + h / 2)
        cv2.rectangle(frame6, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame6, (at, bt), 5, (0, 0, 255), -1)
        cv2.imshow("imagem 7", frame6)

    #----------------------------------------------------------------------------------------------------------------------------
        '''janela 7'''
        frame7 = frame[320:480, 213:426]#primei vem o exixo y depois o x
        mask = cv2.inRange(frame7, rangomin, rangomax)
        # reduce the noise
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        x, y, w, h = cv2.boundingRect(opening)
        at = int(x + w / 2)
        bt = int(y + h / 2)
        cv2.rectangle(frame7, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame7, (at, bt), 5, (0, 0, 255), -1)
        cv2.imshow(" imagem 8", frame7)

    #----------------------------------------------------------------------------------------------------------------------------
        '''janela 8'''
        frame8 = frame[320:480, 426:640]#primei vem o exixo y depois o x
        mask = cv2.inRange(frame8, rangomin, rangomax)
        # reduce the noise
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        x, y, w, h = cv2.boundingRect(opening)
        at = int(x + w / 2)
        bt = int(y + h / 2)
        cv2.rectangle(frame8, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame8, (at, bt), 5, (0, 0, 255), -1)
        cv2.imshow("imagem 9", frame8)

    #----------------------------------------------------------------------------------------------------------------------------

        if cv2.waitKey(1) == ord ("q"):
            break
visao3(vet_leitura)
