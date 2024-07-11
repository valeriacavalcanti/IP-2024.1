estoque = 60
beneficiados = 0

while (estoque > 0):
    h,m,s = input('Tempo: ').split(':')
    h,m,s = int(h), int(m), int(s)

    tempo = h*3600 + m*60 + s

    if (tempo <= (7*3600 + 50*60)):
        pontos = 14
    elif (tempo <= (8*3600 + 40*60)):
        pontos = 8
    elif (tempo <= (9*3600 + 10*60)):
        pontos = 4
    else:
        pontos = 0

    if (pontos > 0):
        beneficiados += 1

    if (pontos <= estoque):
        estoque -= pontos
        falta = 0
    else:
        falta = pontos - estoque
        pontos = estoque
        estoque = 0
        
# Quantidade de alunos beneficiados
print(f'{beneficiados} alunos beneficiados.')

# Quantidade de pontos do último beneficiado
# e se ele recebeu toda a pontuação que merecia
if (falta == 0):
    print(f'Recebeu tudo! {pontos} pontos')
else:
    print(f'Faltou {faltou} pontos')
