import random

# função para gerar n valores [-50,50] aleatórios
# n também é aleatório [1,20], como valor padrão
def aleatorio(n = 0):
    if (n <= 0):
        n = random.randint(1,20)
                
    vetor = [0] * n
    for i in range(n):
        vetor[i] = random.randint(-50,50)
    return vetor

def soma(vetor):
    total = 0
    for num in vetor:
        total = total + num
        # total += num
    return total

# teste
print(aleatorio())
print(aleatorio(0))
print(aleatorio(-1))
print(aleatorio(2))
print(aleatorio(4))
