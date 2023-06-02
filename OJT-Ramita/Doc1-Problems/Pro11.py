'''11. Write a python function with name reverse_vowel that takes one string as an
argument and reverse the order of vowels present in the string. 
The function should return the string having reversed order of vowels. 
For example - If the input string which is given as argument is 'Hello'
then the output string should be 'Holle'. You need to reverse the vowel irrespective of
lowercase or uppercase.'''

def reverse_vowel(st):
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    vowels_in_my_string  = ''
    output = ''
    for i in st:
        if i in vowels:
            vowels_in_my_string += i
    count = 1
    for j in st:
        if j not in vowels:
            output += j
        else:
            output += vowels_in_my_string[-count]
            count += 1
    return output

st = "Hello"
obj = reverse_vowel(st)
print(obj)



# Hello
# eo
# oe
# Holle

# kartikeya
# aiea
# aeia
# kartekiya
