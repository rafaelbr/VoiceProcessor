from dictation import start_stream
from reading import start_reading

def dictate():
    print('Iniciando ditado...')
    start_stream()

def reading():
    print('Iniciando modo de leitura, digite o texto')
    start_reading()

mode = ''

while mode != 'q':
    mode = input('Digite o modo de trabalho (1 para ditado, 2 para leitura, q para finalizar): ')

    if mode == '1':
        #inicia mado ditado
        dictate()
    elif mode == '2':
        #incia modo leitura
        reading()

