'''
    Programa para:
    - gerar 10 números aleatórios e armazenar em um vetor
    - ler um valor do usuário (chute)
    - procurar esse chute no vetor e informar:
        - se achou
'''

import random

numeros = [0] * 10

for i in range(10):
    numeros[i] = random.randint(1,60)

chute = int(input('Chute: '))

# procurar o chute no vetor
for i in range(10):
    if (chute == numeros[i]):
        print('achei')
        break
