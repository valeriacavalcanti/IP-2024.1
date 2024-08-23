import random

matriz = []
for i in range(3):
    matriz.append([0] * 2)

matrizT = []
for i in range(2):
    matrizT.append([0] * 3)

# preencher a matriz com valores aleatórios
for i in range(3):
    for j in range(2):
        matriz[i][j] = random.randint(-5, 5)

# preencher a transporta
for i in range(3):
    for j in range(2):
        matrizT[j][i] = matriz[i][j]

# exibir a matriz
print('Matriz')
for i in range(3):
    print(matriz[i])

# exibir a matriz transposta
print('Matriz transposta')
for i in range(2):
    print(matrizT[i])
