import random

sorteio = [0] * 6
qtd = 0

# gerar 06 valores aleatórios e armazenar no sorteio
for i in range(6):
    sorteio[i] = random.randint(1, 4)

# ler um valor inteiro do usuário
numero = int(input('Número: '))

# calcular a frequência de numero no sorteio
for i in range(6):
    if (numero == sorteio[i]):
        qtd += 1

# exibir a frequência calculada
print(f'{numero} apareceu {qtd} vezes')
