def fatorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod = prod * i
    return prod

def fatorial_2(n):
    if n <= 1:
        return 1
    return n * fatorial_2(n - 1)

# teste
for i in range(11):
    fat1 = fatorial(i)
    fat2 = fatorial_2(i)
    print(f'{i}! = {fat1} - {fat2}')
