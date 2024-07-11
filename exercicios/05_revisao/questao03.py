soma_valores = 0
soma_cupons = 0
maior_valor = -1

for i in range(2):
    valor_compra = float(input('Valor: '))
    cupons = int(valor_compra//30)

    soma_valores += valor_compra
    soma_cupons += cupons

    if (valor_compra > maior_valor):
        maior_valor = valor_compra

    saldo = valor_compra % 30
    #saldo = valor_compra - cupons * 30

    falta = 30 - saldo

    if (cupons > 0):
        print(cupons, 'cupom(ns)')
    else:
        print('sem cupons')
        
    print(f'R$ {saldo:.2f} de saldo')
    print(f'R$ {falta:.2f} para novo cupom')

##
print('------------')
print(f'Total vendido: R$ {soma_valores:.2f}')
print(f'Cupons distribuidos: {soma_cupons}')
cupons = int(maior_valor // 30)
print(f'Maior compra: {maior_valor} ({cupom(ns)} cupons)')

