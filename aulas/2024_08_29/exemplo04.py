'''
Programa para ler um texto e converter esse texto para minúsculo.
'''

original = input('Texto: ')
convertida = ''

for i in range(len(original)):
    cod_original = ord(original[i])

    if (original[i] >= 'A') and (original[i] <= 'Z'):
        cod_min = cod_original + 32
    else:
        cod_min = cod_original
                                
    convertida += chr(cod_min)

print(convertida)
