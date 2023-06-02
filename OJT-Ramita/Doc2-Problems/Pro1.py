'''1.Write a program in which two strings are given and determine if they share a
common substring. A substring may be as small as one character. The function
returns either “YES” or “NO”.'''

def checkSubString(sub, main):
    if sub in main:
        return "YES"
    else:
        return "NO"
    
main_string = "hellomynameiskartik"
sub_string = "my"

obj = checkSubString(sub_string, main_string)
print(obj)

