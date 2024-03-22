maior = -1
menor = 101

for i in range(1,5): # 1 2 3 4 ... 80
    idade = int(input('Idade: '))
    if (idade > maior):
        maior = idade
    if (idade < menor):
        menor = idade

print('Menor:', menor)
print('Maior:', maior)
