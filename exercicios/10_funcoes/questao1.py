def menor(n1, n2, n3):
    if (n1 < n2) and (n1 < n3):
        return n1
    elif (n2 < n3):
        return n2
    else:
        return n3
    

    # teste

print(menor(1, 2, 3)) # 1
print(menor(3, 2, 1)) # 1
print(menor(3, 1, 2)) # 1
print(menor(1,1, 2)) # 1
print(menor(1, 1, 1)) # 1