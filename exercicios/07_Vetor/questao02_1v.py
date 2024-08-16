TAM = 10
notas_validas = []

while (len(notas_validas) < TAM):
    nota = int(input('Nota: '))
    
    # verificar se é válida
    if (nota >= 0) and (nota <= 100):
        notas_validas.append(nota)

# exibir notas válidas que foram lidas
print(notas_validas)
