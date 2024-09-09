while (True):
    num = input('Número: ')

    # validar número
    valido = True
    for simbolo in num:
        if (simbolo <= '0') or (simbolo >= '9'):
            valido = False
            break

    if (valido == True):
        break

print(num)