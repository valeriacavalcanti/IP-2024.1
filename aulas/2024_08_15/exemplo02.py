# declarar matriz 3x4
matriz = []
for i in range(3):
    matriz.append([0]*4)

# exibir TODA a matriz
print(matriz)

# alterar todos os elementos para -1
for i in range(3):
    for j in range(4):
        matriz[i][j] = -1

# exibir TODA a matriz
print(matriz)

# exibir CADA LINHA da matriz
for i in range(3):
    print(i, matriz[i])
    
# exibir CADA ELEMENTO da matriz
for i in range(3):
    for j in range(4):
        print(i, j, '-', matriz[i][j])

        
