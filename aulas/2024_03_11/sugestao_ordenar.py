l1, l2, l3 = input("Lados: ").split()
l1, l2, l3 = float(l1), float(l2), float(l3)

# regra para formar triângulo
# maior lado < soma dos outros lados

if (l1 > l2) and (l1 > l3):
    maior = l1
    if (l2 > l3):
        meio = l2
        menor = l3
    else:
        meio = l3
        menor = l2
else:
    # l1 não é o maior lado
    if (l2 > l3):
        maior = l2
        if (l1 > l3):
            meio = l1
            menor = l3
    else:
        # l1 e l2 não são o maior lado
        maior = l3
        if (l1 > l2):
            meio = l1
            menor = l2
        else:
            meio = l2
            menor = l1

soma = l1 + l2 + l3 - maior

if (maior < soma):
    print('Forma')
else:
    print('Nao forma')
