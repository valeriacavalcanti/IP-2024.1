quantidade = 0

for i in range(6):
    l1, l2, l3 = input('Medidas: ').split()
    l1, l2, l3 = int(l1), int(l2), int(l3)

    if (l1 > l2) and (l1 > l3):
        maior = l1
    else:
        if (l2 > l3):
            maior = l2
        else:
            maior = l3

    soma = (l1 + l2 + l3) - maior

    if (maior < soma):
        quantidade = quantidade + 1

print('Quantidade de pirâmides:', quantidade)