'''2. Given a list of first 10 natural numbers, write a program to find the square of all
even numbers and cube of all odd numbers and store them in another list'''

def findSquareCube(listt):
    squarelst = []
    cubelst = []
    for i in listt:
        if i % 2 == 0:
            squarelst.append(i*i)
        else:
            cubelst.append(i*i*i)
    print("SquareList:", squarelst)
    print("CubeList:", cubelst)      

li = [1,2,3,4,5,6,7,8,9,10]
findSquareCube(li)