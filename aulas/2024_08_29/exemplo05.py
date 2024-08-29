'''
Programa para ler um texto, calcular e exibir:
- Quantidade de letras;
- Quantidade de letras maiúsculas;
- Quantidade de letras minúsculas;
- Quantidade de símbolos numéricos;
- Quantidade de caracteres especiais.
'''

qt_mai = qt_min = qt_num = qt_esp = 0
texto = input('Texto: ')

for i in range(len(texto)):
    if (texto[i] >= 'A') and (texto[i] <= 'Z'):
        qt_mai += 1
    elif (texto[i] >= 'a') and (texto[i] <= 'z'):
        qt_min += 1
    elif (texto[i] >= '0') and (texto[i] <= '9'):
        qt_num += 1
    else:
        qt_esp += 1

print('Letras:', qt_mai + qt_min)
print('Letra maiúsculas:', qt_mai)
print('Letra minúsculas:', qt_min)
print('Símbolos numéricos:', qt_num)
print('Caracteres especiais:', qt_esp)
