hor_i, min_i, seg_i = input().split()
hor_i = int(hor_i)
min_i = int(min_i)
seg_i = int(seg_i)
tinicio = (hor_i * 3600) + (min_i * 60) + seg_i

hor_f, min_f, seg_f = input().split()
hor_f = int(hor_f)
min_f = int(min_f)
seg_f = int(seg_f)
tfim = (hor_f * 3600) + (min_f * 60) + seg_f

tperm = tfim - tinicio

h = tperm //3600
m = (tperm %3600) // 60
s = (tperm %3600) % 60

print(f'{h}:{m}:{s}')