import random

# Declarar a matriz
matriz = []
matrizT = []

for i in range(3):
    matriz.append([0] * 5)

for i in range(5):
    matrizT.append([0] * 3)

# Preencher com valores aleatórios
for i in range(3):
    for j in range(5):
        matriz[i][j] = random.randint(1,100)

# Preencher a transposta
for i in range(5):
    for j in range(3):
        matrizT[i][j] = matriz[j][i]

print(matriz)
print(matrizT)