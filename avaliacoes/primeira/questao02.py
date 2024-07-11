soma = 0
qt = 0
menor = 10*3600

for i in range(57):
    h,m,s = input('Tempo:').split(':')
    h,m,s = int(h), int(m), int(s)

    tempo = h*3600 + m*60 + s

    if (tempo < menor):
        menor = tempo

    if (tempo < (9*3600)):
        qt += 1 # qt = qt + 1

    soma += tempo # soma = soma + tempo


print(f'Quantidade antes das 9h: {qt}')

# Tempo da pessoa que entregou primeiro;

h = menor // 3600
m = (menor % 3600) // 60
s = (menor % 3600) % 60
print(f'Tempo de quem entregou primeiro: {h:02}:{m:02}:{s:02}')

# Média do tempo da turma
media = soma / 57

h = media // 3600
m = (media % 3600) // 60
s = (media % 3600) % 60
print(f'Média da turma: {h:02}:{m:02}:{s:02}')






