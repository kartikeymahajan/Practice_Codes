'''26.Print the pattern Pattern for the input : 3
*1 
21*
*123

Note : Logic should also work for dynamic input - Ex: 5

*1
21*
*123
4321*
*12345
'''
n = 9

flag = True
for i in range(1,n+1):
    temp = ""
    if flag:
        for j in range(1,i+1):
            temp += str(j)
        print(f"*{temp}")
        flag = False
    else:
        for j in range(1, i+1):
            temp += str(j)
        print(f"{temp[::-1]}*")
        flag = True

