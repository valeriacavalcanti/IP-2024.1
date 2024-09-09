import random

soma_turma = 0
maior = -1
qtd_acima = 0

# Declarar a matriz de notas
notas = []
for i in range(20):
    notas.append([0] * 3)

# Ler/Gerar as notas
for i in range(20):
    for j in range(3):
        notas[i][j] = random.randint(0,100)
        # Somar todas as notas lidas
        soma_turma += notas[i][j]
        # Verificar maior nota lida
        if (notas[i][j] > maior):
            maior = notas[i][j]

media_turma = soma_turma / (20*3)

# Calcular a média de cada aluno
for i in range(20):
    soma_aluno = 0
    for j in range(3):
        soma_aluno += notas[i][j]
    media_aluno = soma_aluno / 3
    print(f'Aluno {i} - Média: {media_aluno:.0f}')
    if (media_aluno > media_turma):
        qtd_acima += 1

print(f'Maior nota: {maior}')
print(f'Quantidade alunos c/ média acima da turma: {qtd_acima}')