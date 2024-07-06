nota = int(input('Informe uma nota: '))
maior = menor = nota

while (nota >= 0) and (nota <= 100):
    if (nota > maior):
        maior = nota
    elif (nota < menor):
        menor = nota
    nota = int(input('Informe uma nota: '))

if (maior < 0) or (maior > 100):
    print('Nenhum valor digitado')
else:
    print('menor =', menor)
    print('maior =', maior)