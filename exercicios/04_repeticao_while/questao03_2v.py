# VERSÃO: LOOP INFINITO

import random

erros = 0
valor_aleatorio = random.randint(1,100)

while (True):
    chute = int(input('Chute: '))

    if (chute == valor_aleatorio):
        break

    erros = erros + 1


print('Acertou!')
print(f'Errou {erros} vezes!')