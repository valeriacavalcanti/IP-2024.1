# VERSÃO: LOOP INFINITO

arrecadacao = 0
quantidade = 0

while (True):
    doacao = float(input('Doação: '))
    quantidade = quantidade + 1
    arrecadacao = arrecadacao + doacao
    
    if (arrecadacao >= 1000):
        break

extra = arrecadacao - 1000

print(f'Arrecadação: R% {arrecadacao:.2f}')
print(f'Quantidade de doações: {quantidade}')
print(f'Valor extra arrecadado: {extra:.2f}')