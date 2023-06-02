'''28. Given a string s and an integer k, reverse the first k characters for every 2k
characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k
but greater than or equal to k characters, then reverse the first k characters 
and leave the other as original.
Input: s = abcdefg, k = 2
Output:    bacdfeg
Input: s = abcd, k = 2
Output:    bacd'''

def reverseString(s, k):
    strLen = len(s)
    output = ""
    left = 0
    rev = False
    for i in range(strLen):
        if i % k == 0:
            subStr = s[left:i]
            if rev:
                subStr = subStr[::-1]
            output += subStr
            left = i
            rev = not rev
    subStr = s[left:strLen]
    if rev:
        subStr = subStr[::-1]
    output += subStr
    return output

s = "abcdefg"
k= 2
obj = reverseString(s,k)
print(obj)

