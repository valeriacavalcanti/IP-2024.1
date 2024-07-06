# VERSÃO: CONDIÇÃO NO LOOP

import random

erros = 0
valor_aleatorio = random.randint(1,100)

chute = int(input('Chute: '))
while (chute != valor_aleatorio):
    erros = erros + 1
    chute = int(input('Chute: '))

print('Acertou!')
print(f'Errou {erros} vezes!')