def tempo_permanencia (h,m,s):
    hor_i, min_i, seg_i = 7,0,0
    tinicio = (hor_i * 3600) + (min_i * 60) + seg_i   
    hor_f, min_f, seg_f = h,m,s
    tfim = (hor_f * 3600) + (min_f * 60) + seg_f
    tperm = tfim - tinicio
    return tperm

def tempo_restante (h,m,s):
    hor_t, min_t, seg_t = 9,30,0
    ttermino = (hor_t * 3600) + (min_t * 60) + seg_t   
    hor_f, min_f, seg_f = h,m,s
    tfim = (hor_f * 3600) + (min_f * 60) + seg_f
    trestante = ttermino - tfim
    return trestante

def permanencia(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += tempo_permanencia(matriz[i][0],matriz[i][1],matriz[i][2])
    tperm = soma // len(matriz)
    return tperm

def print_data(seg):
    h = seg // 3600
    m = (seg % 3600) // 60
    s = (seg % 3600) % 60
    print(f'{h}:{m}:{s}')

# Programa Pricipal

LIN = 3
COL = 3
alunos = []
for i in range(LIN):
    alunos.append([0] * COL)
    
for i in range(LIN):
    h, m, s = input(f'hora minuto segundo - {i+1}: ').split()
    alunos[i][0] = int(h)
    alunos[i][1] = int(m)
    alunos[i][2] = int(s)

print('Tempo que restou de prova para cada aluno: ')
for i in range(LIN):
    tr = tempo_restante(alunos[i][0],alunos[i][1],alunos[i][2])
    print(f'Aluno {i}:')
    print_data(tr)
    
media = permanencia(alunos)
print('\nMedia do tempo de permanencia da turma: ')
print_data(media)