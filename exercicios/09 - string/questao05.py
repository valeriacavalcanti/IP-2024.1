texto = input('Texto: ')
letras = []

for simbolo in texto:
    if ((simbolo >= 'a') and (simbolo <= 'z')):
        # converter para maiúscula
        simbolo = chr(ord(simbolo) - 32)

    if ((simbolo >= 'A') and (simbolo <= 'Z')):
        if (simbolo not in letras):
            letras.append(simbolo)

print(letras)