votos_sim = 0
votos_nao = 0
votos_invalidos = 0

for i in range(80):
    voto = input('Informe seu voto: ')
    if (voto == 'SIM'):
        votos_sim = votos_sim + 1
    elif (voto == 'NAO'):
        votos_nao = votos_nao + 1
    else:
        votos_invalidos = votos_invalidos + 1

porcentagem_sim = votos_sim/80 * 100
porcentagem_nao = votos_nao/80 * 100
porcentagem_invalidos = votos_invalidos/80 * 100

print(f'Votos SIM: {porcentagem_sim:.2f}%')
print(f'Votos NAO: {porcentagem_nao:.2f}%')
print(f'Votos Inválidos: {porcentagem_invalidos:.2f}%')