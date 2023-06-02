s = ["H","a","n","n","a","h"]
n = len(s)//2
print(n)
for i in range(n):
    temp = s[i]
    s[i] = s[-(i+1)]
    s[-(i+1)] = temp

print(s)