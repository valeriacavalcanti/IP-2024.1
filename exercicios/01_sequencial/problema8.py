valor_compra = float(input("Valor da compra: "))

cupons = int(valor_compra // 30)

saldo = valor_compra % 30
#saldo = valor_compra - (cupons * 30)

valor_acrescentar = 30 - saldo

print(cupons, 'cupons')

print(f"R$ {saldo:.2f}")
#print("R$ {:.2f}".format(saldo))

print(f"R$ {valor_acrescentar:.2f}")
#print("R$ {:.2f}".format(valor_acrescentar))