'''18. Write a python program where for every two hours it prints the pattern without using
sleep function
 **********
  ********
   ******
    ***
     *
    '''

from threading import Event

def stars(n):
    for i in range(n,0,-1):
        for j in range(0, n-i):
            print(end=" ")
        for j in range(0,i):
            print("*", end=" ")
        print()

for i in range(5):
    stars(7)
    Event().wait(3)