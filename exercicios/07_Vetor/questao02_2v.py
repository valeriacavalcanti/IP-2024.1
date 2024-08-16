TAM = 4
notas_validas = [0] * TAM

# preencher o vetor com notas válidas
for i in range(TAM):

    # ler uma nota candidata
    nota = int(input('Nota: '))
    
    # validar essa nota candidata
    while (nota < 0) or (nota > 100):
        nota = int(input('Nota: '))

    # armazenar no vetor a nota validada
    notas_validas[i] = nota

# exibir as notas válidas que foram armazenadas
print(notas_validas)
