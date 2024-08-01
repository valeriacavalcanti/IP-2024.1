# 15/07/2024
# 15/7/2024

dia, mes, ano = input('Data: ').split('/')
dia, mes, ano = int(dia), int(mes), int(ano)

data = ano + mes + dia
outra_forma = f"{ano}{mes:02}{dia:02}"

print(dia, mes, ano)
print(data)
print(outra_forma)
