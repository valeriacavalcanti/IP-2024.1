arq = open('nomes.txt','w')

for i in range(4):
    nome = input('Nome: ')
    arq.write(f'{nome}\n')

arq.close()

print('terminou')
