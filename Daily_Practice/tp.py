def ValidPalindrome(st: str)->bool:
    new = ""
    for i in st:
        if i.isalnum():
            new+=i
    reverse = new[::-1]
    print(new)
    print(reverse)
    if new.lower() == reverse.lower():
        return True
    else:
        return False

st = "A man, a plan, a canal: Panam"
op = ValidPalindrome(st)
print(op)
