soma = 0

for i in range(6):
    numero = int(input('Número: '))
    soma = soma + numero

media = soma / 6

#print(f"Média = {media:.2f}")
print("Média = {:.2f}".format(media))