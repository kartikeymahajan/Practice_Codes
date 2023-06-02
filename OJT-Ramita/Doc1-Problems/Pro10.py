'''10. In the given String -- 'MsYs TecHNOlogiEs iS a gREat place To woRk' find the
count of lowercase and uppercase letters.'''

st = "MsYs TecHNOlogiEs iS a gREat place To woRk"
lower = 0
upper = 0
for i in st:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1

print("Uppercase letters are:", upper)
print("Lowercase letters are:", lower)

