def print_e(texto, n = 0):
    for i in range(len(texto) - 1):
        print(texto[i], ' '*n, sep='', end='')
    print(texto[i + 1])

## teste
print_e('IFPB')
print_e('IFPB', 1)
print_e('IFPB', 2)
