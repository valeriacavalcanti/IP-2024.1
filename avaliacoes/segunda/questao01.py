import random

numeros = [0] * 10
for i in range(10):
    numeros[i] = random.randint(1, 20)

pos = -1
for i in range(10):
    if (numeros[i] == 12):
        pos = i
        break

if (pos >= 0):
    print(f'Tem o número 12 no índice {pos}')
else:
    print('Não tem o número 12')