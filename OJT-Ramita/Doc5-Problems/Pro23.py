'''23. Print the followint pattern
    *
   *_*
  *___*
 *_____*
*_______*

'''
# n = 10
# print(" "*n,"*")
# for i in range(2,n):
#     print(" "*(n-i),"*", end="")
#     for j in range(1, n):
#         print("_"*j,"*")


row = int(input("Enter the row number: "))

for i in range(row):
    for j in range(row-i):
        print(' ', end='')

    for j in range(2*i+1):
        if j==0 or j==2*i:
            print('*',end='')
        else:
            print('_', end='')
    print()