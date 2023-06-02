'''9.Given a string "abcde", Display the output as "a1b2c3d4e5"'''

st = "abcde"
new_st = ""

for i in range(len(st)):
    new_st = new_st + st[i]+str(i+1)

print(new_st)