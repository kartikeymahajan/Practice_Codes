def ValidPalindrome(st: str)->bool:
    new = ""
    for i in st:
        if i.isalnum():
            new+=i
    reverse = new[::-1]
    return new.lower() == reverse.lower()

st = "A man, a plan, a canal: Panama"
op = ValidPalindrome(st)
print(op)