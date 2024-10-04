TAM = 4
tperm = [0] * TAM
soma = 0

hor_i, min_i, seg_i = 7,0,0
hor_i = int(hor_i)
min_i = int(min_i)
seg_i = int(seg_i)
tinicio = (hor_i * 3600) + (min_i * 60) + seg_i

for i in range(TAM):
    hor_f, min_f, seg_f = input(f'hora minuto segundo - {i+1}: ').split()
    hor_f = int(hor_f)
    min_f = int(min_f)
    seg_f = int(seg_f)
    tfim = (hor_f * 3600) + (min_f * 60) + seg_f
    tperm[i] = tfim - tinicio
    soma += tperm[i]

media = soma // TAM

h = media // 3600
m = (media %3600) // 60
s = (media %3600) % 60

print(f'Tempo medio de permanencia: {h}:{m}:{s}')

qt = 0
for i in range(TAM):
    if tperm[i] < media:
        qt += 1

print(f'Alunos que entregaram antes da média de tempo: {qt}')