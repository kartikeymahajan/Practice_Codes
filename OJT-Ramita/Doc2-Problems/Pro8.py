'''8. Write Row class that accepts any keyword arguments given to it and stores these
arguments as attributes.
Ex. >>> row = Row(a=1, b=2)
>>> row.a
1
>>> row.b
2'''

class Row():
    def __init__(self,a,b):
        self.a = a
        self.b = b

obj = Row(20, 30)
print(obj.a)
print(obj.b)

