TAM = 4
frutas = [''] * TAM
repetiu = False

# ler as frutas
for i in range(TAM):
    frutas[i] = input('Fruta: ')

# calcular a frequência de cada fruta
for i in range(TAM):
    fruta = frutas[i]
    qt = 0
    for j in range(TAM):
        if (fruta == frutas[j]):
            qt += 1
    if (qt > 1):
        repetiu = True
        break
    #print(f'{fruta} apareceu {qt} vezes')

if (repetiu == True):
    print('Tem fruta repetida')
else:
    print('Não houve repetição')
    
            
