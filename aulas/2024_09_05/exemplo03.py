"""
Programa para ler um texto e exibir:
- quantidade de vogais
"""

qtd = 0
vogais = 'AEIOU'
texto_original = input('Texto: ')
texto_maiusculo = texto_original.upper()

"""
qtd = texto_maiusculo.count('A')
qtd += texto_maiusculo.count('E')
qtd += texto_maiusculo.count('I')
qtd += texto_maiusculo.count('O')
qtd += texto_maiusculo.count('U')
"""
for vogal in vogais:
    qtd += texto_maiusculo.count(vogal)

print(qtd)

