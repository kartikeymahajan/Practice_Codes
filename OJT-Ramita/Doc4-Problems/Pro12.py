'''
12.Solve the following scenarios·
• Let's assume that there is a tuple containing username, You have got a requirement to 
add password also into it.
oInput : ("user1")
oOutput: ("user1","password1 ")'''

oInput = ("user1")
password = "password1"

oInput = tuple([oInput]+[password])

print(oInput)


'''
• Below logic is failing with an error message, Instead of auto generated Error, 
Please display the user defined message saying "Error : Cannot concatenate String and Number"·
print("msys" + 2007)'''


try:
    print("msys"+2007)
except:
    print("Error : Cannot concatenate String and Number")


