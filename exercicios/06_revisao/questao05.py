dia, mes, ano = input('Data: ').split('/')
maior = int(f'{ano}{mes:02}{dia:02}')
maior_dia = dia
maior_mes = mes
maior_ano = ano

for i in range(2):
    dia, mes, ano = input('Data: ').split('/')
    tempo = int(f'{ano}{mes:02}{dia:02}')

    if (tempo > maior):
        maior_dia = dia
        maior_mes = mes
        maior_ano = ano

print(f'Maior Data: {maior_dia}/{maior_mes}/{maior_ano}')
