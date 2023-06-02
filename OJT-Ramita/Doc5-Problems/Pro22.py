n = 5
for i in range(1,n):
    for j in range(0, n-i):
        print(" ", end = "")
    print(f"{i} "*i)
for i in range(n-2, 0, -1):
    for j in range(n-i, 0, -1):
        print(" ", end="")
    print(f"{i} "*i)
