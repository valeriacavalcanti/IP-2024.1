# Declarar as matrizes
matriz_a = []
matriz_b = []
matriz_c = []

for i in range(2):
    matriz_a.append([0]*4)
    matriz_b.append([0]*4)
    matriz_c.append([0]*4)

# Ler Matriz A
for i in range(2):
    for j in range(4):
        matriz_a[i][j] = int(input(f'A[{i}][{j}]: '))

# Ler Matriz B
for i in range(2):
    for j in range(4):
        matriz_b[i][j] = int(input(f'B[{i}][{j}]: '))

# Calcular Matriz C
for i in range(2):
    for j in range(4):
        matriz_c[i][j] = matriz_a[i][j] + matriz_b[i][j]

# Exibir todas as matrizes
print(matriz_a)
print(matriz_b)
print(matriz_c)