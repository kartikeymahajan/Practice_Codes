'''8.Write a function in Python that accepts a credit card number. It should return a 
string where all the characters are hidden with an asterisk except the last four.
For eg., if the credit card no. is “4509876278910046”, then function should 
return “************0046”
'''

def hideCredit(num):
    result = ""
    str_num = str(num)
    temp = len(str_num)-4

    # approach 1
    # for i in range(len(str_num)):
    #     if i < temp:
    #         result += "*"
    #     else:
    #         result += str_num[i]

    # approach 2
    # result = "*" * temp + str_num[-4:]
    
    return result

obj = hideCredit(1234567890123456)
print(obj)
