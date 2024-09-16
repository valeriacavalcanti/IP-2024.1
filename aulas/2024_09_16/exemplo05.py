arq = open('apostas.txt', 'r')

# arq.readlines()           # vem com \n
# arq.read().splitlines()   # nao vem com \n

apostas = arq.read().splitlines()
for linha in apostas:
    print(linha.split())

arq.close()
