"""
    Modulo de comunicação Serial com o arduino, responsavel por estabelecer a comunicação e enviar dados.

"""

import serial
import subprocess

_porta = serial.Serial()


# Funcao de envio na serial.
# Converte os dados para o tipo 'bytes'.
def enviaSerial(comando):
    comando = str(comando)
    for c in range(0, len(comando)):
        envia = str.encode(comando[c])
        _porta.write(envia)
    _porta.write(b'\n')


def ler():
    lido = _porta.readline()
    print(lido)
    return str(lido)


def limpa_cache():
    _porta.flush()


def aguarda_ok():
    while True:
        limpa_cache()
        if ler() != 'Ok':
            continue
        else:
            break
    return True


# funcao para listar as portas seriais disponiveis, funciona em windows e linux.
def lista_select():
    from sys import platform
    if platform == 'linux':
        nome = '/dev/'
    elif platform == 'win32':
        nome = 'COM'
    else:
        print('sistema nao suportado')
        pass
    # Inicia o processo que lista as portas seriais.
    lst = str(subprocess.Popen(['python', '-m', 'serial.tools.list_ports'], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).communicate())
    # quebra a string em uma lista.
    lst = lst.split('\\n')
    # formatação da lista, apenas para estetica.
    try:
        for c in range(0, len(lst) - 1):
            if nome in lst[c]:
                lst[c] = lst[c].strip('(').strip('b').strip('\'').strip('\\').strip(')').strip('\\r').strip()
                print('{} = {}'.format(c, lst[c]))
            else:
                lst.remove(lst[c])
    except IndexError:
        for c in range(0, len(lst) - 2):
            if nome in lst[c]:
                lst[c] = lst[c].strip('(').strip('b').strip('\'').strip('\\').strip(')').strip('\\r').strip()
                print('{} = {}'.format(c, lst[c]))
            else:
                lst.remove(lst[c])
    port = int(input('Digite o numero correspondente a porta: '))
    return str(lst[port])


def setName(nome):
    _porta.port = nome


def setRate(rate):
    _porta.baudrate = rate


# Abre a porta serial
def inicia():
    _porta.open()


# fecha a porta serial.
def fecha():
    _porta.close()
