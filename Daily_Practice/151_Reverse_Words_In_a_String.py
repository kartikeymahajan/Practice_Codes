def ReverseWords(st: str)->str:
    reverse =" "
    li = list(st.split(" "))
    temp = li[::-1]
    reverse = reverse.join(temp)
    return reverse

st = input("Enter a string: ")
op = ReverseWords(st)
print(op)