import funcoes

qt_maiusculas = int(input("Quantidade de letras maiúsculsa: "))
qt_minusculas = int(input("Quantidade de letras minúsculas: "))
qt_numericos = int(input("Quantidade de símbolos numéricos: "))

senha = funcoes.senha(qt_maiusculas, qt_minusculas, qt_numericos)

super_senha = funcoes.super_senha(senha)

print(f'Senha gerada: {senha}')
print(f'Super senha gerada: {super_senha}')