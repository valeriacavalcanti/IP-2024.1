'''
    Programa para:
    - gerar 10 números aleatórios e armazenar em um vetor
    - ler um valor do usuário (chute)
    - procurar esse chute no vetor e informar:
        - se achou ou não
        - índices onde encontrou esse chute no vetor (estratégia: vetor de marcação)
'''

import random

QTD = 10
numeros = [0] * QTD
qt_encontrado = 0

for i in range(QTD):
    numeros[i] = random.randint(1,10)

chute = int(input('Chute: '))

# atualizar o vetor de marcação
marcacao = [False] * QTD
for i in range(QTD):
    if (chute == numeros[i]):
        marcacao[i] = True
        qt_encontrado += 1

# exibir a marcação (onde encontrei chute)
print("Quantidade encontrada:", qt_encontrado)
for i in range(QTD):
    if (marcacao[i] == True):
        print(f'Índice: {i} - Valor: {numeros[i]}')
        
