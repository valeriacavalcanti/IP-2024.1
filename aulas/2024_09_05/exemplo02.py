"""
Programa para ler um texto e exibir:
- quantidade de palavras
"""

qtd = 0
texto = input('Texto: ')

qtd = texto.count(' ')

if (len(texto) > 0):
    qtd += 1

print(qtd)
