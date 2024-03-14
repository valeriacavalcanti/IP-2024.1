valor = float(input('Valor: '))

if (valor <= 100):
    aliquota = 4
else:
    # valor acima de 100
    if (valor <= 200):
        aliquota = 6
    else:
        # valor acima 200
        if (valor <= 400):
            aliquota = 8
        else:
            # valor acima 400
            aliquota = 10

cashback = valor * (aliquota / 100)
print('Alíquota: ',aliquota,'%', sep='')
print('R$ {:.2f} de Cashback'.format(cashback))
