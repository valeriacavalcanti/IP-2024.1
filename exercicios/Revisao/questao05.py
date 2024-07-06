soma_valores = 0
soma_cupons = 0
maior_valor = -1
cupons_maior_valor = 0
estoque = 1000
clientes_felizes = 0
faltou_entregar = 0

while (estoque > 0):
    valor_compra = float(input('Valor: '))
    cupons = int(valor_compra//30)

    if (cupons <= estoque):
        estoque -= cupons
        if (cupons > 0):
            clientes_felizes += 1
    else:
        # nao consegue entregar todos os cupons
        faltou_entregar = cupons - estoque
        cupons = estoque
        estoque = 0

    soma_valores += valor_compra
    soma_cupons += cupons

    if (valor_compra > maior_valor):
        maior_valor = valor_compra
        cupons_maior_valor = cupons

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
print(f'Maior compra: {maior_valor} ({cupons_maior_valor} cupom(ns))')
print('------------')
print(f'{clientes_felizes} receberam todos os cupons')
if (faltou_entregar == 0):
    print('Tudo certo!')
else:
    print(f'Faltou {faltou_entregar} cupons para 1 cliente')
