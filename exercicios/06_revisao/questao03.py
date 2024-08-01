# PRIMEIRO É O MAIOR
maior = int(input('Número: '))
  
for i in range(3):
    numero = int(input('Número: '))

    # SE O NÚMERO FOR O MAIOR -> ATUALIZA OS DOIS
    if (numero > maior):
        segundo_maior = maior
        maior = numero
    elif (i == 0): # SEGUNDO NÚMERO LIDO
        segundo_maior = numero
    elif (numero > segundo_maior): # DEMAIS VALORES LIDOS
        segundo_maior = numero

print(f'Segundo maior valor: {segundo_maior}')
