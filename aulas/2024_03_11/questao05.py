mes = int(input('Mês: '))

if (mes == 2):
    print('29 dias')
else:
    # mês não é 2 (FEV)
    if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        print('30 dias')
    else:
        # mês não e 2, 4, 6, 9, 11
        print('31 dias')
