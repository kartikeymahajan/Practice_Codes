'''16. Write a function which will take a string argument and reverse the words in the string. 
For example - Input string -- “Hello World”. Output should be “olleH dlroW”.'''

def reverseString(st):
    li = st.split(" ")
    for i in range(len(li)):
        li[i] = li[i][::-1]
    return " ".join(li)

st = "Hello World"
obj = reverseString(st)
print(obj)

# Using Lambda function
# def reverseString(st):
#     li = st.split(" ")
#     lam = list(map(lambda x: x[::-1], li))
#     return " ".join(lam)