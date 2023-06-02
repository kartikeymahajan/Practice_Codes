'''21. You are given a string and width. Your task is to wrap the string into paragraph of
width in reverse order. Blank spaces should be ignored.
for eg: i/p - first line contains a string with blank spaces - 
Hello, welcome to 
this
organisation. 
the second line conatins the width - 4
o/p
lleH
ew,o
mocl
tote
osih
nagr
tasi
.noi'''

import textwrap

st = '''Hello, welcome to 
this
organisation.'''

st = " ".join(st.split())
li = st.split(" ")
for i in range(len(li)):
    li[i] = li[i][::-1]

st = " ".join(li)

print(textwrap.fill(st,4))