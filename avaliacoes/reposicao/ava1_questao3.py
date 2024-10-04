QTD = 20
fatias = QTD
cli = 0
soma = 0

while True:
    if (fatias == 0):
        break
    n_fatias = int(input('Num. fatias: '))
    if n_fatias > 10:
        n_fatias = 10
    if n_fatias > fatias:
        n_fatias = fatias
    fatias -= n_fatias
    cli += 1
    soma += n_fatias

print(f'Clientes que receberam fatias: {cli}')
print(f'Média por cliente = {soma//cli} fatias')