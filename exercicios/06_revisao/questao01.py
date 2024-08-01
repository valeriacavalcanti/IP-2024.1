menor_idade = None
nome_maior_altura = idade_maior_altura = maior_altura = None
soma = qt = 0

for i in range(3):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    altura = int(input('Altura: '))

    if (i == 0) or (idade < menor_idade):
        menor_idade = idade

    if (i == 0) or (altura > maior_altura):
        maior_altura = altura
        nome_maior_altura = nome
        idade_maior_altura = idade

    if (altura > 165):
        qt += 1
        soma += idade

print(f'Idade da pessoa mais nova: {menor_idade}')
print(f'Pessoa mais alta: {nome_maior_altura} - {idade_maior_altura}')

