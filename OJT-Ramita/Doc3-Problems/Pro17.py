'''17. Write a program to find the count of alphabet alone in the given alphanumeric string for
Ex1: input=’abb24ccc8ddbbca1’ output=’a1b224c3d2b2c1a11’
Ex2: input = ‘abc23’ output=’a1b1c123’'''

def findAlphaCount(s):
    op = ""
    count = 1
    for i in range(len(s)):
        if i>=len(s):
            break
        elif s[i].isalpha():
            op += s[i]
            while s[i] == s[i+1]:
                count += 1
                s = s[:i]+s[i+1:]
            op += str(count)     
            count = 1
        elif s[i].isdigit():
            op += s[i]
    return op

s = 'abb24ccc8ddbbca1'
obj = findAlphaCount(s)
print(obj)