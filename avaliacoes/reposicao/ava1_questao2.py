TAM = 3
tempo = [0] * TAM
tprim = 9999999999
soma = 0

for i in range(TAM):
    h,m,s = input(f'hora minuto segundo - {i+1}: ').split()
    h,m,s = int(h),int(m),int(s)
    tempo[i] = (h * 3600) + (m * 60) + s
    if (tempo[i] < tprim):
        tprim = tempo[i]
    soma += tempo[i]

h = tprim // 3600
m = (tprim % 3600) // 60
s = (tprim % 3600) % 60

print(f'O primeiro chegou em {h}:{m}:{s}')

media = soma // TAM
h = media // 3600
m = (media % 3600) // 60
s = (media % 3600) % 60

print(f'Media de tempo de chegada = {h}:{m}:{s}')