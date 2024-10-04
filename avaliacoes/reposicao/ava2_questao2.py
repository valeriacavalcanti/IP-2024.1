import random
TAM = 20
distintos = []
repet = []
num = [0] * TAM

for i in range(TAM):
    num[i] =random.randint(1,10)
    if num[i] not in distintos:
        distintos.append(num[i])
        repet.append(1)
    else:
        ind = distintos.index(num[i])
        repet[ind] +=1

print('Numeros gerados: ', num)
print ('numeros sem repetição: ',distintos)
print('\nFrequencia de repetição por numero: ')
for i in range(len(distintos)):
    print(distintos[i],'-',repet[i])
