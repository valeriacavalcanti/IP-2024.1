import random
TAM = 5

# declarar a matriz de notas
notas = []
for i in range(TAM):
    notas.append([0] * 3)

# atribuir a pontuação "da sorte"
for i in range(TAM):
    for j in range(3):
        notas[i][j] += random.randint(0,40)

# exibir as notas, por linha (aluno)
for i in range(TAM):
    print(i, notas[i])

# exibir as notas, por linha (aluno), com a soma das notas
for i in range(TAM):
    soma = 0
    for j in range(3):
        soma += notas[i][j]
    print(i, notas[i], soma)

# exibir a pontuacao distribuida por nota
for i in range(3):
    soma = 0
    temp = []
    for j in range(TAM):
        soma += notas[j][i]
        temp.append(notas[j][i])
    print(i, temp, soma)

    
# somar o total da pontucao distribuida - geral!!
soma = 0
for i in range(TAM):
    for j in range(3):
        soma += notas[i][j]
print(soma)

# descobrir os valores distintos presentes na matriz
distintos = []
for i in range(TAM):
    for j in range(3):
        if (notas[i][j] not in distintos):
            distintos.append(notas[i][j])

print(distintos)
