valor_produto = float(input('Valor do produto: '))
quantidade = int(input("Quantidade: "))

total = valor_produto * quantidade

print(f"R$ {total:.2f}")
#print("R$ {:.2f}".format(total))