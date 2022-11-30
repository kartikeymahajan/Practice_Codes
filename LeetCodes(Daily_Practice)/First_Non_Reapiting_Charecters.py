st = "acaba"
new = ""

for i in st:
    count = 0
    for j in st:
        if i == j:       #check for repeated characters
            count+=1
        if count > 1:    #if character is found more than 1 time brerak the loop
            break
    if count == 1:       #concatenation of all nonrepeating characters
        new = new + i

print(new[-1])           #printing first nonrepeating character