soma = 0
qt = 0
qt_acima = 0
#numeros = [0] * 6
numeros = [0,0,0,0,0,0]

# percorrer o vetor: escrever e ler
for i in range(6):
    numeros[i] = int(input('Número: '))
    if (numeros[i] > 20):
        qt = qt + 1
        #qt += 1
    soma = soma + numeros[i]
    #soma += numeros[i]

media = soma / (i + 1)

# percorrer o vetor (ler)
# verificar se o elemento armazenado é acima da média
for i in range(6):
    if (numeros[i] > media):
        qt_acima = qt_acima + 1
        #qt_acima += 1

print('Soma:', soma)
print('Média', media)
print('Quantidade acima de 20:', qt)
print('Quantidade acima da média:', qt_acima)

# exibir todos os valores lidos!
for i in range(6):
    print(i, numeros[i])


print(numeros)

# DOBRAR os valores que estão armazenados no vetor
for i in range(6):
    numeros[i] = numeros[i] * 2

print(numeros)

numeros[2] = numeros[2] * 2
print(numeros)
