class StackArrays:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def isempty(self):
        return len(self._data)==0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return 
        else:
            return self._data.pop()
    
    def top(self):
        if self.isempty():
            print("Stack is empty")
            return 
        else:
            return self._data[-1]

s = StackArrays()
s.push(5)
s.push(10)
s.push(15)
print(s._data)
print(s.__len__()) 
print(s.isempty())
s.pop()
print(s._data)
print(s.__len__()) 
print(s.top())
