class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0
    
    def addlast(self, e):
        new = _Node(e, None)
        if self.isempty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

    def addfirst(self, e):
        new = _Node(e, None)
        if self.isempty():
            self._head = new
        else:
            new._next = self._head
            self._head = new
        self._size += 1

    def addany(self, e, position):
        new = _Node(e, None)
        p = self._head
        count = 1
        while count < position -1:
            p = p._next
            count +=1
        new._next = p._next
        p._next = new
        self._size += 1
    
    def removefirst(self):
        if self.isempty():
            print("List is empty..")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._tail = None
        print("Removed Item:",e)

    def removelast(self):
        if self.isempty():
            print("List is empty..")
            return
        p = self._head
        count = 1
        while count < len(self) -1:
            p = p._next
            count +=1
        e = p._next._element
        self._tail = p
        p._next = None
        self._size -= 1
        print("Removed Item: ",e)

    def removeany(self, position):
        if self.isempty():
            print("List is empty..")
            return
        count = 1
        p = self._head
        while count < position-1:
            p = p._next
            count +=1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        print("Removed Item:",e)

    def search(self, item):
        p = self._head
        index = 0
        while p:
            if item == p._element:
                return index
            p = p._next
            index += 1 
        return -1
            

    def display(self):
        d = self._head
        while d:
            print(d._element, end=', ')
            d = d._next
        print()

obj = LinkedList()

obj.addlast(2)
obj.addlast(5)
obj.addlast(17)
obj.addlast(45)
obj.display()
size = obj.__len__()
print("Size:",size)

se = obj.search(17)
print("Index:",se)