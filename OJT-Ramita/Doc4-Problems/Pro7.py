'''7 In the given string, remove the special characters and add a space instead of 
 "Msys&Technologies@Chennai*"'''

st = "Msys&Technologies@Chennai*"
print(st)

for i in st:
    if not i.isalpha():
        st = st.replace(i, " ")

print(st)