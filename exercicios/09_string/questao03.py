texto = input('Texto: ')

existe = False

for simbolo in texto:
    if (simbolo >= 'a') and (texto <= 'z'):
        existe = True
        break

if (existe == True):
    print('Existe letra minuscula')
else:
    print('Nao xiste letra minuscula')