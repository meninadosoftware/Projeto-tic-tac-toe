import sr_driver as porta


porta.setName('COM3')
porta.setRate(115200)
porta.inicia()

while True:
    porta.enviaSerial("teste")
    print(porta.ler())

print('Finalizado')
