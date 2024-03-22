soma_vendas = 0
soma_cashback = 0

for i in range(400):
    venda = float(input('Venda: '))
    soma_vendas = soma_vendas + venda

    if (venda <= 100):
        cashback = venda * 0.04
    elif (venda <= 200):
        cashback = venda * 0.06
    elif (venda <= 400):
        cashback = venda * 0.08
    else:
        cashback = venda * 0.1
    
    soma_cashback = soma_cashback + cashback

#print(f'Total das vendas: R$ {soma_vendas:.2f}')
print('Total das vendas: R$ {:.2f}'.format(soma_vendas))

#print(f'Total de Cashback: R$ {soma_cashback:.2f}')
print('Total das Cashback: R$ {:.2f}'.format(soma_cashback))
