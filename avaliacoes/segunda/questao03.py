refeicoes = []

for i in range(30):
    refeicoes.append([0] * 4)


# ler o valor calórido de cada refeicao
for i in range(30):
    for j in range(4):
        refeicoes[i][j] = int(input('Valor calórico: '))


# Total de calorias consumida por dia
for i in range(30):
    soma = 0
    for j in range(4):
        soma += refeicoes[i][j]
    print(f'Dia {i + 1} = {soma} calorias.')


# Total de calorias consumidas por refeição
for j in range(4):
    soma = 0
    for i in range(30):
        soma += refeicoes[i][j]
    print(f'Refeição {j + 1} = {soma} calorias')