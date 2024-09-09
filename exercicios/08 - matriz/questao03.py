import random

# Declarar a Matriz
matriz = []
for i in range(40):
    matriz.append([0]*6)

# Preencher com valores aleatórios
for i in range(40):
    for j in range(6):
        matriz[i][j] = random.randint(1,20)

maior = 0
menor = 21

num = int(input('Digite um valor: '))
qtd = 0

# Procurar esse número na matriz
# Descobrir o maior e o menor valor
for i in range(40):
    for j in range(6):
        if (matriz[i][j] == num):
            qtd += 1
        if (matriz[i][j] < menor):
            menor = matriz[i][j]
        if (matriz[i][j] > maior):
            maior = matriz[i][j]

# Exibir
print(f'{num} aparece {qtd} vezes')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')