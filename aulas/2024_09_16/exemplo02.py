import random

def gerar_aposta(qt, menor, maior):
    if ((maior - menor + 1) >= qt):
        vetor = []
        while (len(vetor) < qt):
            numero = random.randint(menor, maior)
            if (numero not in vetor):
                vetor.append(numero)
        return vetor
    else:
        return []

def aposta_str_1v(aposta):
    aposta.sort()
    # aposta é uma lista
    st = f'{aposta[0]}'
    for num in aposta[1:]:
        st += f' {num}'
    return st
        
    
# PP

arq = open('apostas.txt', 'w')

for i in range(100):
    #arq.write(str(gerar_aposta(6, 1,60)))
    aposta = gerar_aposta(6, 1,60)
    aposta_str = aposta_str_1v(aposta)
    arq.write(f'{aposta_str}\n')

arq.close()


