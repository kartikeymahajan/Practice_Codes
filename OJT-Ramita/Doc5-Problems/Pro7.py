'''7.Reverse the below string without changing the position of special characters . 
s      = "adfw$vf&yvy*ugv%uy" 
output = "yuvg$uy&vyf*vwf%da"
'''

s = "adfw$vf&yvy*ugv%uy" 

def func(s):

    di = {}
    result = ""
    reverse = s[::-1]

    for i in range(len(s)):
        if not s[i].isdigit() and not s[i].isalpha():
            di[i] = s[i]

    for i in range(len(s)):
        if reverse[i].isalpha() or reverse[i].isdigit():
            result += reverse[i]
        if i in di:
            result += di[i]
        
    print(result)
print(s)
func(s)




