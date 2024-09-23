candidatos = [0] * 442
votados = []
invalidos = 0

# cadastrar os números dos candidatos
for i in range(442):
    candidatos[i] = int(input('Número: '))


# ler os votos dos eleitores
for i in range(2000):
    voto = int(input('Voto: '))
    if (voto in candidatos):
        if (voto not in votados):
            votados.append(voto)
    else:
        invalidos += 1

print(f'Quantidade de candidatos que receberam votos: {len(votados)}')
print(f'Quantidade de votos nulos: {invalidos}')