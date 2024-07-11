h,m,s = input('Tempo: ').split(':')
h,m,s = int(h),int(m),int(s)

tempo = h * 3600 + m * 60 + s

tempo_falta = (9*3600 + 30*60) - tempo

h = tempo_falta // 3600
m = (tempo_falta % 3600) // 60
s = (tempo_falta % 3600) % 60

print(f'{h:02}:{m:02}:{s:02}')
