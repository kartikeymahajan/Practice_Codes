'''13. Write a function that accepts a string containing lines of numbers and returns a
list of lists of numbers.
Ex. matrix_from_string("3 4 5")
[[3.0, 4.0, 5.0]]'''

def convert(st):
    s = st.split(" ")
    output = []
    for i in s:
        output.append(float(i))
    return [output]

matrix_from_string = '''3 4 5 
5 6 7'''
obj = convert(matrix_from_string)
print(obj)

