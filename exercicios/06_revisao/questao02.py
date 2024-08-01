maior_par = None

num = int(input('Digite um número: '))
while (num != 0):
    if (num % 2 == 0) and ((maior_par == None) or (num > maior_par)):
        maior_par = num

    num = int(input('Digite um número: '))

if (maior_par == None):
    print('Nenhum valor par digitado')
else:
    print(f'Maior valor par: {maior_par}')

