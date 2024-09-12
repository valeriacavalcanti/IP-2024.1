def soma(vetor):
    soma_valores = 0
    for elem in vetor:
        soma_valores += elem
    return soma_valores

# teste
print(soma([])) # 0
print(soma([10])) # 10
print(soma([10, 20])) # 30
print(soma([10, 20 , 30])) # 60