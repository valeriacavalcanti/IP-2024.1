sopa = 1000
qt = 0

copo = int(input('Copo: '))
while (sopa - copo > 0):
    qt = qt + 1
    sopa = sopa - copo
    copo = int(input('Copo: '))

faltou = copo - sopa
qt = qt + 1

print(f'Beneficiados: {qt}')

if (faltou > 0):
    print(f'O ultimo beneficiado foi incompleto, faltou {faltou} ml.')
else:
    print('Todos satisfeitos!')