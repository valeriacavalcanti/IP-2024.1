# a primeira idade será a menor e a maior

idade = int(input('Idade: '))
#maior = menor = idade
maior = idade
menor = idade

# as demais idades serão verificadas
for i in range(1,4):
    idade = int(input('Idade: '))
    if (idade > maior):
        maior = idade
    if (idade < menor):
        menor = idade

print('Menor =', menor)
print('Maior =', maior)
