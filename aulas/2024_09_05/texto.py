# Contar as vogais em um texto
def contar_vogais(texto):
    qtd = 0
    vogais = 'AEIOU'
    texto = texto.upper()
    for vogal in vogais:
        qtd += texto.count(vogal)
    return qtd

# Contar as letras maiúsculas em um texto
def contar_maiusculas(texto):
    qtd = 0
    for i in range(len(texto)):
        if (texto[i].isupper() == True):
            qtd += 1
    return qtd

# Contar as letras minúsculas em um texto
def contar_minusculas(texto):
    qtd = 0
    for i in range(len(texto)):
        if (texto[i].islower() == True):
            qtd += 1
    return qtd

# Contar os números em um texto
def contar_numeros(texto):
    qtd = 0
    for i in range(len(texto)):
        if (texto[i].isdigit() == True):
            qtd += 1
    return qtd

# Verificar se o texto contém apenas números
def isNumero(texto):
    for s in texto:
        if (s < '0') or (s > '9'):
            return False
    return True
