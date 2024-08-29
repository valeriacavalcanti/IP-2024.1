'''
Programa para ler um texto e exibir:
- índice do símbolo no texto
- símbolo do texto
- código decimal do símbolo do texto
- código binário do símbo do texto
'''

nome = input('Melhor instituicao: ')

for i in range(len(nome)):
    print(i, nome[i], ord(nome[i]), bin(ord(nome[i]))[2:])
