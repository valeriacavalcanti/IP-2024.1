texto = input('Texto: ')
palavras = []
frequencia = []
texto_maiusculo = ''

# converter para maiúsculo
for simbolo in texto:
    if (simbolo >= 'a') and (simbolo <= 'z'):
        texto_maiusculo += chr(ord(simbolo) - 32)
    else:
        texto_maiusculo += simbolo

# contar palavras
for palavra in texto_maiusculo.split():
    if (palavra not in palavras):
        palavras.append(palavra)
        frequencia.append(1)
    else:
        for i in range(len(palavras)):
            if (palavra == palavras[i]):
                frequencia[i] += 1
                break

print('Texto original:', texto)
print('Texto convertido para maiúsculo:', texto_maiusculo)

for i in range(len(palavras)):
    print(f'{palavras[i]} = {frequencia[i]}')