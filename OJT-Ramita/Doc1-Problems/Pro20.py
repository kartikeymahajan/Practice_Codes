'''20. You are given a string having alphabets,digits,special characters. Write three
different functions to extract the digits[should be in sorted order], 
special character & vowels[should be in reverse] from the given string.

i/p string : "abcd123bye09@8"
o/p: digits - 012389
special character - @
vowels - ea '''

def extractDigits(st):
    li = []
    for i in st:
        if i.isdigit():
            li.append(i)
    output = ''.join(sorted(li))
    print("digits -",output)

def extractSpecialChars(st):
    op = ''
    for i in st:
        if i.isdigit() == False and i.isalpha() == False:
            op += i
    print("special character -", op[::-1])

def extractVowels(st):
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    op = ''
    for i in st:
        if i in vowels:
            op += i 
    print("vowels -", op[::-1])

st = "abcd123bye09@8"
extractDigits(st)
extractSpecialChars(st)
extractVowels(st)




# import re
# def digit(s):
#     d= re.findall("\d",s)
#     print("Digits: {}".format("".join(d)))
# def vowel(s):
#     v= re.findall("a|e|i|o|u", s)
#     print("Vowels: {}".format("".join(v)))
# def char(s):
#     c= re.findall("\W",s)
#     print("Special Characters: {}".format("".join(c)))
# s="abcd123bye09@8"
# digit(s)
# char(s)
# vowel(s)