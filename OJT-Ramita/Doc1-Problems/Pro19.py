'''19. Write a function which takes input string from the user as argument and the
character also taken by the user as the argument and remove all the occurences of 
that character from the string. Also if the given character is not present in the 
string your function should raise the exception stating that
“Given character is not present in the string. Please try with a new one”.'''

def removeChars(string, s):
    counter = 0
    flag = True
    while counter < (len(string)):
        temp = string[counter]
        if string[counter] == s:
            string = string[:counter]+string[counter+1:]
            counter -= 1
            flag = False
        counter += 1
    if flag:
        raise Exception("Given character is not present in the string. Please try with a new one")
    print(string)
string = "karatiakeya"
s = "a"
removeChars(string, s)
