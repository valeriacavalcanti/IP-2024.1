'''
    Programa para:
    - gerar 10 números aleatórios e armazenar em um vetor
    - ler um valor do usuário (chute)
    - procurar esse chute no vetor e informar:
        - se achou ou não
        - índices onde encontrou esse chute no vetor (estratégia: vetor com os índices)
'''

import random

QTD = 10
numeros = [0] * QTD
posicoes = []

for i in range(QTD):
    numeros[i] = random.randint(1,6)

chute = int(input('Chute: '))

# procurar chute
for i in range(QTD):
    if (chute == numeros[i]):
        posicoes.append(i)

if (len(posicoes) == 0):
    print('nao tem')
else:
    print('Encontrei:', len(posicoes))
    print(posicoes)

# Posições e valores que estão nas respectivas posições
for i in range(len(posicoes)):
    print(f'Índice: {posicoes[i]} - {numeros[posicoes[i]]}')
