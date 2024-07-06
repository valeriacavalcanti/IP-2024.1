# VERSÃO: CONDIÇÃO NO LOOP

arrecadacao = 0
quantidade = 0

while (arrecadacao < 1000):
    doacao = float(input('Doação: '))
    quantidade = quantidade + 1
    arrecadacao  = arrecadacao + doacao

extra = arrecadacao - 1000

print(f'Arrecadação: R% {arrecadacao:.2f}')
print(f'Quantidade de doações: {quantidade}')
print(f'Valor extra arrecadado: {extra:.2f}')