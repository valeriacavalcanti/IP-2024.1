import random

LIN = 4
COL = 6
matriz = []
pontos = []
primeiro = 0

for i in range(LIN):
    matriz.append ([0] * COL)

for i in range(LIN):
    soma = 0
    for j in range(COL):
        matriz[i][j] = random.randint(1,10)
        soma += matriz[i][j]
    pontos.append(soma)
    if soma > primeiro:
        primeiro = soma
        indp = i

print(f'Primeiro colocado foi o ginasta {indp+1} com {primeiro} pontos:')
for i in range(LIN):
    print(f'diferença do primeiro colocado:',primeiro - pontos[i])