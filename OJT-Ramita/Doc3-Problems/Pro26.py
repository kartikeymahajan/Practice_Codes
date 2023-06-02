'''26. You are given a string S. Your task is to find the indices of the start and end of string k in
S The first line contains the string S.The second line contains the string k.
Print the tuple in this format: (start _index, end _index). If no match is found, print (-1,
-1).
Sample Input Sample Output
aaadaa
aa
(0, 1)
(1, 2)
(4, 5)'''
just = main_str = "aaadaa"
sub_str  = "aa"

# for i in range(len(main_str)):
#     if sub_str in just and sub_str[0]==just[i]:
#         index = just.find(sub_str)
#         print((index, index +len(sub_str)-1))
#     just = just[:i]+"*"+just[i+1:]


for i in range(len(main_str)):
    for j in range(len(sub_str)):
        if sub_str[j] == main_str[j]:
            temp = j
        else: print((i, temp))

