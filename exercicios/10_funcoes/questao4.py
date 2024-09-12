def fatorial(num):
    fat = 1
    for i in range(1, num + 1):
        fat = fat * i
    return fat

# teste

for i in range(6):
    print(i, fatorial(i))