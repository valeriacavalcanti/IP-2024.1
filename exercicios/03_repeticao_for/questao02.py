validas = 0

for i in range(8):
    nota = int(input('Nota: '))
    if (nota >= 0) and (nota <= 100):
        validas = validas + 1

#print(f'Foram informadas {validas} notas válidas para o Suap.')
print('Foram informadas {} notas válidas para o Suap.'.format(validas))