'''
Programa para ler um texto e exibir (convertendo para minúsculo, quando possível):
- índice do símbolo no texto
- símbolo do texto
- código decimal do símbolo do texto
- código binário do símbo do texto
'''

# VERSÃO 2.0 (usando os códigos dos símbolos no 'if')

nome = input('Melhor instituicao: ')

for i in range(len(nome)):
    cod_original = ord(nome[i])

    if (ord(nome[i]) >= 65) and (ord(nome[i]) <= 90):
        cod_min = cod_original + 32
    else:
        cod_min = cod_original
                                
    print(i, nome[i], cod_original, cod_min, chr(cod_min))
