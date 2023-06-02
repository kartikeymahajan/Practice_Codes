'''6. Write a program to extract the words starting with lowercase letter present in the
list. ['Nissan', 'maruti', 'hyundai', 'Volkswagen', 'audi']'''

li = ['Nissan', 'maruti', 'hyundai', 'Volkswagen', 'audi']

for i in li:
    if i[0].islower():
        print(i, end=", ")

