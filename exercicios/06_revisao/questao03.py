# PRIMEIRO É O MAIOR
maior = int(input('Número: '))
  
for i in range(3):
    numero = int(input('Número: '))

    # Se o número for maior -> atualiza os dois
    if (numero > maior):
        segundo_maior = maior
        maior = numero
    elif (i == 0) or (numero > segundo_maior): # é o segundo número lido OU o número é maior do que o segundo maior valor
        segundo_maior = numero

print(f'Segundo maior valor: {segundo_maior}')
