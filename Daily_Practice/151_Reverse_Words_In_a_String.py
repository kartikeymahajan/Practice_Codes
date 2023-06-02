def ReverseWords(st: str)->str:
    li = list(st.split(" "))
    temp = li[::-1]
    reverse = " ".join(temp)
    reverse = " ".join(reverse.split())
    return reverse

st = "My name is     kartik"
op = ReverseWords(st)
print(op)