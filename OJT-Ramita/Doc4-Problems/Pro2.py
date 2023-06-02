'''2.Define a function which returns a list contains only the palindrome strings from the 
list of provided string elements

input	: List of strings
output : List of palindrome strings'''

def findPalindrome(li):
    op = []
    for i in li:
        if i.upper() == i[::-1].upper():
            op.append(i)
    return op

li = ["Nayan", "Kartik", "1001", "nitin", "Ram"]
obj = findPalindrome(li)
print(obj)

