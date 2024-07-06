valor_compra = float(input('Valor: '))
cupons = int(valor_compra//30)

saldo = valor_compra % 30
#saldo = valor_compra - cupons * 30

falta = 30 - saldo

if (cupons > 0):
    print(cupons, 'cupons')
else:
    print('sem cupons')
print(f'R$ {saldo:.2f} de saldo')
print(f'R$ {falta:.2f} para novo cupom')



