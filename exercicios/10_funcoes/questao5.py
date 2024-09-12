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
    media = media_final(n1, n2, n3)
    if (media >= 80):
        return 'A'
    elif (media >= 60):
        return 'B'
    elif (media >= 40):
        return 'C'
    else:
        return 'D'
    
# teste
#print(media_aritmetica(90,80,70))
#print(media_ponderada(90,80,70))
#print(media_final(90,80,70))
#print(conceito(90,80,70))

# programa principal
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

print(f'Média = {media_aritmetica(nota1, nota2, nota3)}')
print(f'Conceito = {conceito(nota1, nota2, nota3)}')