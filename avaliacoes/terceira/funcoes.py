import random

def consoantes(texto):
    distintos = ''
    vogais = 'AEIOU'
    for simbolo in texto.upper():
        if (simbolo >= 'A') and (simbolo <= 'Z') and (simbolo not in vogais) and (simbolo not in distintos):
            distintos += simbolo
    return distintos


def somador(texto):
    soma = 0
    for simbolo in texto:
        if (simbolo >= '0') and (simbolo <= '9'):
            soma += int(simbolo)
    return soma


def senha(maiusculas, minusculas, numericos):
    texto = ''

    for i in range(maiusculas):
        texto += chr(random.randint(ord('A'), ord('Z')))

    texto += '#'

    for i in range(minusculas):
        texto += chr(random.randint(ord('a'), ord('z')))

    texto += '$'

    for i in range(numericos):
        texto += str(random.randint(0, 9))

    return texto


def super_senha(texto):
    return consoantes(texto) + str(somador(texto))