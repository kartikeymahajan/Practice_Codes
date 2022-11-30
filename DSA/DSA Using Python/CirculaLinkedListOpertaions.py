class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class CircularLinkedList:
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
            new._next = new
            self._head = new 
        else:
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1

    def addfirst(self, e):
        new = _Node(e, None)
        if self.isempty():
            new._next = new
            self._head = new
            self._tail = new
        else:
            self._tail._next = new
            new._next = self._head
        self._head = new
        self._size += 1 

    def addany(self, e, position):
        new = _Node(e, None)
        p = self._head
        count = 1
        while count < position - 1:
            p = p._next
            count += 1
        new._next = p._next
        p._next = new
        self._size += 1

    def removelast(self):
        if self.isempty():
            print('List is empty')
            return
        p = self._head
        count = 1
        while count < len(self) -1:
            p = p._next
            count += 1
        e = p._next._element
        self._tail = p
        self._tail._next = self._head
        self._size -= 1
        return e

    def removefirst(self):
        if self.isempty():
            print('List is empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._tail._next = self._head
        self._size -= 1
        if self.is_empty():
            self._head = None
            self._tail = None
        return e
    
    def removeany(self, position):
        p = self._head
        count = 1
        while count < position -1:
            p = p._next
            count += 1
        e = p._next._element
        p._next = p._next._next
        self._size -=1
        return e

    def search(self, item):
        p = self._head
        count = 0
        while count < len(self):
            if item == p._element:
                return count
            p = p._next
            count += 1
        return -1

    def display(self):
        p = self._head
        count = 0
        while count < len(self):
            print(p._element, end=', ')
            p = p._next
            count += 1
        print()

obj = CircularLinkedList()
obj.addlast(5)
obj.addlast(7)
obj.addlast(15)
obj.addlast(56)
obj.addlast(98)

obj.display()
s = obj.__len__()
print('Size:', s)

r = obj.search(7)
print(f"The item is on index {r}")