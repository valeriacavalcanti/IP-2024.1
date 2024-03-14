'''
    Programa para ler 10 números inteiros.
    Calcular e exibir quantos são:
        - positivos
        - negativos
        - zero
'''

qt_negativo = 0
qt_positivo = 0
qt_zero = 0

soma = 0

for i in range(6):
    num = int(input('Número: '))
    soma = soma + num
    
    if (num > 0):
        #print('positivo')
        qt_positivo = qt_positivo + 1
    else:
        if (num < 0):
            #print('Negativo')
            qt_negativo = qt_negativo + 1
        else:
            #print('Zero')
            qt_zero = qt_zero + 1

# exibir as quantidades encontradas
print('Positivos:', qt_positivo)
print('Negativos:', qt_negativo)
print('Zeros:', qt_zero)

print('Soma =', soma)
