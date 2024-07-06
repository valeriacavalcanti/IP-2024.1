# VERSÃO: CONDIÇÃO NO LOOP

soma = 0
qt = 0

numero = int(input('Número: '))
while (numero != 0):
    soma = soma + numero
    qt = qt + 1
    numero = int(input('Número: '))

if (qt > 0):
    media = soma / qt
    print(f'Média = {media:.2f}')
else:
    print('Nenhum valor digitado')