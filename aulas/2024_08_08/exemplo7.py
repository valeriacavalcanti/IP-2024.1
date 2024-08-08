'''
    Programa para:
    - gerar 10 números aleatórios e armazenar em um vetor
    - exibir os valores pares que estão no vetor
    - exibir os valores que estão nos índices pares do vetor
'''

import random

QTD = 10
numeros = [0] * QTD

for i in range(QTD):
    numeros[i] = random.randint(1,6)

# exibir os valores "pares"
print('Números pares')
for i in range(QTD):
    if (numeros[i] % 2 == 0):
        print(numeros[i])

# exibir os valores que estão nos índices pares
print('Números nos índices pares')
for i in range(QTD):
    if (i % 2 == 0):
        print(numeros[i])


# exibir os valores que estão nos índices pares
print('Números nos índices pares')
for i in range(0, QTD, 2):
    print(numeros[i])
        
