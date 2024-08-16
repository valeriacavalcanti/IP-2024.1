# programa para ler as 02 notas de 03 alunos

# declarar a matriz de notas
notas = []
for i in range(3):
    notas.append([0] * 2)

# ler TODAS as notas de TODOS os alunos
for i in range(3):
    for j in range(2):
        notas[i][j] = int(input(f'Aluno {i+1} - Nota {j+1}: '))

# exibir TODAS as nota
print(notas)

# exibir as notas de CADA aluno e respectiva média
for i in range(3):
    print(f'Aluno {i+1}, Notas: {notas[i]}')
    # somar as notas DO aluno
    soma = 0
    for j in range(2):
        soma += notas[i][j]
    # calcular a média DO aluno
    media = soma / 2
    # exibir a média DO aluno
    print(f'Média: {media:.2f}')


# calcular a média da PRIMEIRA nota
soma = 0
for i in range(3):
    soma += notas[i][0]

media = soma / 3

print(f'Média da primeira nota: {media:.2f}')

# calcular quantos passaram por média
qtd = 0
for i in range(3):
    soma = 0
    for j in range(2):
        soma += notas[i][j]
    media = soma / 2
    if (media >= 70):
        qtd += 1

# exibir quantos passaram por média
print(f'{qtd} alunos passaram por média')


# verificar se alguém tirou 100
existe = False
for i in range(3):
    for j in range(2):
        if (notas[i][j] == 100):
            existe = True
            break
    if (existe == True):
        break

if (existe == True):
    print('Tem nota 100')
else:
    print('Não tem nota 100')
