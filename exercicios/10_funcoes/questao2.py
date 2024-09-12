def print_e(texto, n):
    for i in range(len(texto) - 1):
        print(texto[i], end=' ' * n)
    print(texto[i + 1])

# teste
print_e('TESTANDO', 0) # TESTANDO
print_e('TESTANDO', 1) # T E S T A N D O
print_e('TESTANDO', 2) # T  E  S  T  A  N  D  O
print_e('TESTANDO', 4) # T    E    S    T    A    N    D    O