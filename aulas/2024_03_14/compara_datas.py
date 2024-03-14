dia, mes, ano = input('Data: ').split('/')
dia, mes, ano = int(dia), int(mes), int(ano)

if (ano > 2024):
    print('Futuro')
else:
    if (ano < 2024):
        print('Passado')
    else:
        # ano é 2024!
        if (mes > 3):
            print('Futuro')
        else:
            if (mes < 3):
                print('Passado')
            else:
                # mês é 3 (março)
                if (dia > 14):
                    print('Futuro')
                else:
                    if (dia < 14):
                        print('Passado')
                    else:
                        # dia é 14
                        print('Presente')
