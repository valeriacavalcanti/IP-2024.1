qtd = 0
valores_2023 = [0] * 12

# ler os valores do ano passado
for i in range(12):
    valores_2023[i] = float(input('Valor: '))

# ler o valor atual
valor_atual = float(input('Valor atual: '))

# contar quantas vezes atual é inferior ao ano passado
for i in range(12):
    if (valor_atual < valores_2023[i]):
        qtd += 1

print(qtd)
