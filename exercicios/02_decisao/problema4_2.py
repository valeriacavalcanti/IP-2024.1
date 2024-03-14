valor = float(input("Valor da compra: "))

if (valor <= 100):
    aliquota = 4
elif (valor <= 200):
    aliquota = 6
elif (valor <= 400):
    aliquota = 8
else:
    aliquota = 10


cashback = valor * (aliquota/100)

print(f'Alíquota: {aliquota}%')
print(f'R$ {cashback:.2f} de Cashback')