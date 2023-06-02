'''20. Write a python program for sort the given below list based last character of each word
names_list = ['Prabhu', Rahul', 'Arunesh, 'Sonali', 'Rakshit']'''

names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']

for i in range(len(names_list)-1):
    for j in range(i, len(names_list)-1):
        if names_list[i][-1]> names_list[j][-1]:
            temp = names_list[i]
            names_list[i] = names_list[j]
            names_list[j] = temp
print(names_list)

# names_list[1] = "Unnu"
# print(names_list)