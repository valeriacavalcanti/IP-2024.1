'''
    Programa para:
    - gerar 10 números aleatórios e armazenar em um vetor
    - ler um valor do usuário (chute)
    - procurar esse chute no vetor e informar:
        - se achou ou não
'''

import random

QTD = 10
numeros = [0] * QTD

for i in range(QTD):
    numeros[i] = random.randint(1,20)

chute = int(input('Chute: '))

# procurar o chute no vetor
existe = False
for i in range(QTD):
    if (chute == numeros[i]):
        existe = True
        break

if (existe == True):
    print('achei')
else:
    print('não achei')
