def media_aritmetica(n1, n2, n3):
    return (n1 + n2 + n3) // 3

def media_ponderada(n1, n2, n3):
    return (n1 * 2 + n2 * 4 + n3 * 6) // 12

def media_final(n1, n2, n3):
    ma = media_aritmetica(n1, n2, n3)
    mp = media_ponderada(n1, n2, n3)
    if (ma > mp):
        return ma
    else:
        return mp

def conceito(n1, n2, n3):
    mf = media_final(n1, n2, n3)
    if (mf >= 80):
        return 'A'
    elif (mf >= 60):
        return 'B'
    elif (mf >= 40):
        return 'C'
    else:
        return 'D'

# teste
#print(media_aritmetica(90,80,70)) #80
#print(media_ponderada(90,80,70)) #76
#print(media_final(90,80,70)) #80
#print(conceito(90,80,70)) #A
#print(conceito(0,0,0)) #D

## PP
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

media = media_final(nota1, nota2, nota3)
conceito_final = conceito(nota1, nota2, nota3)

print(f'Média = {media} e Conceito = {conceito_final}')
