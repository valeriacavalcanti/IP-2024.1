'''
    Programa para:
    - gerar 10 números aleatórios e armazenar em um vetor
    - ler um valor do usuário (chute)
    - procurar esse chute no vetor e informar:
        - se achou ou não
        - caso tenha achado, qual é a posição
'''

import random

QTD = 10
numeros = [0] * QTD

for i in range(QTD):
    numeros[i] = random.randint(1,20)

chute = int(input('Chute: '))

# procurar o chute no vetor
posicao = -1
for i in range(QTD):
    if (chute == numeros[i]):
        posicao = i
        break

if (posicao != -1):
    print('achei na posicao', posicao)
else:
    print('não achei')
