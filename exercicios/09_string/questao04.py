texto = input('Texto: ')

vogais = 'AEIOaeiou'
qtd = 0

for simbolo in texto:
    if (simbolo in vogais):
        qtd += 1

print(f'Quantidade de vogais: {qtd}')