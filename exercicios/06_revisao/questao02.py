maior_par = None

# LER PRIMEIRO VALOR PAR
num = int(input('Número: '))
while (num != 0 and num % 2 == 1):
    num = int(input('Número: '))

if (num != 0) and (num % 2 == 0):
    # LER DEMAIS VALORES
    maior_par = num
    num = int(input('Número: '))
    while (num != 0):
        if (num % 2 == 0) and (num > maior_par):
            maior_par = num
        num = int(input('Número: '))

if (maior_par == None):
    print('Nenhum valor par digitado')
else:
    print(f'Maior valor par: {maior_par}')

