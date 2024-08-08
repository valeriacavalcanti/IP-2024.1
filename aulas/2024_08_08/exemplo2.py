'''
    Programa para:
    - gerar 10 números aleatórios e armazenar em um vetor
    - ler um valor do usuário (chute)
    - procurar esse chute no vetor e informar:
        - se achou
        - caso tenha achado, qual é a posição
'''

import random

QTD = 10
numeros = [0] * QTD

for i in range(QTD):
    numeros[i] = random.randint(1,20)

chute = int(input('Chute: '))

# procurar o chute no vetor
for i in range(QTD):
    if (chute == numeros[i]):
        break

if (i < (QTD - 1)) or ((i == QTD - 1) and numeros[i] == chute):
    print('achei no índice', i)
else:
    print('não achei')
