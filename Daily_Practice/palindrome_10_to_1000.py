li = []

def palindrome(x,y):
    for n in range(x, y):
        if n == int(str(n)[::-1]):
            li.append(n)
    print(li)

palindrome(10,100)
