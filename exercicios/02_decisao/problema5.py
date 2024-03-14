mes = int(input('Mês: '))

if (mes == 2):
    print('29 dias')
else:
    if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        print('30 dias')
    else:
        print('31 dias')