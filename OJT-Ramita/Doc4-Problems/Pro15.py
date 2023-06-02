'''15.Define logic for generating the random password with the provided 
length as an input'''

import random
import string

def generatePassword(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

generatePassword(8)
generatePassword(6)
generatePassword(4)