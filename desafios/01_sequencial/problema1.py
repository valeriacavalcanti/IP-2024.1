hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
segundo = int(input("Segundo: "))

# 1 hora = 60 minutos = 3600 segundos
# 1 minuto = 60 segundos

tempo = hora * 3600 + minuto * 60 + segundo

print(tempo)