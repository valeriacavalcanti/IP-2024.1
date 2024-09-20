def senha(nome,idade):
  lista = nome.split()
  sh = ''
  for i in range(len(lista)):
    sh = sh + lista[i][0]
  sh = sh +str(idade)
  return sh

def media(idades):
  soma = 0
  for idade in idades:
    soma += idade
  midade = soma // len(idades)
  return midade

def menor(idades):
  menidade = idades[0]
  for i in range(len(idades)):
    if idades[i] < menidade:
      menidade = idades[i]
  return menidade

def ind_menor_idade(idades):
  m = menor(idades)
  ind_menores = []
  for i in range(len(idades)):
    if idades[i] == m:
      ind_menores.append(i)
  return ind_menores

def cashback(valor,limite, p):
  cashb = 0
  if valor >= limite:
    cashb = valor * (p / 100)
  return cashb
  
# Programa Principal
#print(senha('ALVARO DIAS PEIXOTO',20))
#print(media([12,20,26,32]))
#print(menor([21,13,42,23,21]))
#print(ind_menor_idade([21,13,42,13,23,21,13]))
print(cashback(400,500,10))