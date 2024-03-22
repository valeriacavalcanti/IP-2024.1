maior = menor = int(input('Idade: '))

for i in range(40):
    idade = int(input('Idade: '))
    if (idade > maior):
        maior = idade
    elif (idade < menor):
        menor = idade

print('Menor idade:', menor)
print('Maior idade:', maior)