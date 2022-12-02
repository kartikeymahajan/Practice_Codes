def fabonacci(num):
    n1, n2 = 0, 1
    if num <= 0:
        print("Please enter a positive number...")
    elif num == 1:
        print(0)
    else:
        print("Fabonacci Sequence: ", end="")
        for i in range(0,num):
            print(n1, end=", ")
            nth = n1 + n2
            n1 = n2
            n2 = nth

fabonacci(2)