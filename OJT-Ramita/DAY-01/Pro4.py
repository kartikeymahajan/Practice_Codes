'''Write a program to find the count of alphabet alone in the given alphanumeric string for
Ex1: input='abb24ccc8ddbbca1' output='a1b224c3d2b2c1a11'
Ex2: input = 'abc23' output='a1b1c123' '''

# import time

# start = time.time()

# Solution One
# def findAlphaCount(s):
#     op = ""
#     count = 1
#     for i in range(len(s)):
#         if i>=len(s):
#             break
#         elif s[i].isalpha(): #2
#             op += s[i]
#             while s[i] == s[i+1]: # b == b
#                 count += 1
#                 s = s[:i]+s[i+1:]
#             op += str(count)     
#             count = 1
#         elif s[i].isdigit():
#             op += s[i]
#     return op

# s = 'abb24ccc8ddbbca1'
# obj = findAlphaCount(s)
# print(obj)


input1='abb24ccc8ddbbca1'
count=1
char1=''
str1=''
for i in input1:  
    if(i.isalpha()): 
        if i!=char1:
            char1=i
            count=1
            str1=str1+i+str(count)
        else:
            # count=count+1
            str1=str1[:(len(str1)-1)]     #a1b1 [a1b]
            count+=1
            str1=str1+str(count)      
    else:
        if i.isdigit():
            str1=str1+i
print(input1)
print(str1)

# end = time.time()

# print(f"Runtime of the program is {end - start}")