class DEqueArrays:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def addfirst(self, e):
        self._data.insert(0, e)
    
    def addlast(self, e):
        self._data.append(e)

    def removefirst(self):
        if self.isempty():
            print("DEQue is empty")
            return 
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._data.pop()

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

d = DEqueArrays()
d.addlast(1)
d.addlast(3)
d.addlast(5)
print(d._data)

d.addfirst(0)
print(d._data)

print(d.isempty())
print("First",d.first())
print("Last", d.last())

print("First item removed", d.removefirst())
print("last item removed", d.removelast())

print(d._data)
print(d.__len__())