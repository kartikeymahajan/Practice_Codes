# Program 1
# li = [3,1,2,4]
# count = 0
# while count < len(li):
#     if len(li)//2 == count:
#         break
#     else:
#         if li[count]%2 != 0:
#             temp = li[count]
#             li.remove(temp)
#             li.append(temp)
#             count -= 1
#     count += 1

# print(li)


# Program 2
# n1 = '1131'
# n2 = '1'
# count = 0
# op = 0
# while count < len(n1):
#     if n1[count]==n2:
#         n1 = n1[:count]+n1[count+1:]
#         temp = int(n1)
#     if temp>=op:
#         op = temp
#     count += 1
# print(op)


# Program 3
# st = "Hello, python is fun and coding, compilation is GOOD Practice in Free Time"
# consonants = 0
# for i in range(len(st)):
#     if st[i] in ["a", "A", "e", "E", "i", "I", "o","O", "u", "U"]:
#         st = st[:i]+"_"+st[i+1:]
#     else:
#         consonants += 1

# print(st)
# print(consonants)



# Program 4
# t=(1,1,2,34,5,6,7,7,4,3,66,4,6,7,8)
# output = {}

# t = set(t)
# t = sorted(list(t))

# for i in range(1,len(t)+1):
#     output[i] = t[-i]**2

# print(output)