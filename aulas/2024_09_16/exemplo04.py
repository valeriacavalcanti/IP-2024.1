arq = open('apostas.txt', 'r')

texto1 = arq.read()
arq.seek(0)
texto2 = arq.read()

print(texto1)
print('--------------------------')
print(texto2)

arq.close()
