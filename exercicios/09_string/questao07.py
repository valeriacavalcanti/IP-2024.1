texto = input('Texto: ')

# Verificar se existe apenas letras maiúsculas
maiuscula = True
for simbolo in texto:
    if (simbolo <= 'A') or (simbolo >= 'Z'):
        maiuscula = False
        break

if (maiuscula == True):
    print('Apenas maiúsculas')
else:
    print('Misturado')