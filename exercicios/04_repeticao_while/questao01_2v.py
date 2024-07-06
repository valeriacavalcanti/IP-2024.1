# VERSÃO: LOOP INFINITO

soma = 0
qt = 0

while (True):
    numero = int(input('Número: '))
    if (numero == 0):
        break
    soma = soma + numero
    qt = qt + 1

if (qt > 0):
    media = soma / qt
    print(f'Média = {media:.2f}')
else:
    print('Nenhum valor digitado')