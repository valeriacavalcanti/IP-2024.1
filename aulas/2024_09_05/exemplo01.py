"""
Programa para ler um texto e exibir:
- quantidade de palavras
"""

qtd = 0
texto = input('Texto: ')

for i in range(len(texto)):
    if (texto[i] == ' '):
        qtd += 1

if (len(texto) > 0):
    qtd += 1

print(qtd)
