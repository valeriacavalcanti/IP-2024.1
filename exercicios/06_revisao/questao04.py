dia1, mes1, ano1 = input('Primeira Data: ').split('/')
tempo1 = int(f'{ano1}{mes1:02}{dia1:02}')

dia2, mes2, ano2 = input('Segunda Data: ').split('/')
tempo2 = int(f'{ano2}{mes2:02}{dia2:02}')

if (tempo1 > tempo2):
    print(f'{dia1}/{mes1}/{ano1}')
else:
    print(f'{dia2}/{mes2}/{ano2}')
