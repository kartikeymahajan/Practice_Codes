from platform import node

from numpy import empty


class _Node:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0
    
    def addlast(self, e):
        new = _Node(e, None, None)
        if self.isempty():
            self._head = new
            self._tail = new
        else:
            self._tail._next = new
            new._prev = self._tail
            self._tail = new
        self._size += 1

    def addfirst(self, e):
        new = _Node(e, None, None)
        if self.isempty():
            self._head = new
            self._tail = new
        else:
            self._head._prev = new
            new._next = self._head
            self._head = new
        self._size +=1

    def addany(self, e, position):
        new = _Node(e, None, None)
        p = self._head
        count = 1
        while count < position-1:
            p = p._next
            count += 1
        new._next = p._next
        new._prev = p
        p._next._prev = new
        p._next = new
        self._size +=1
    
    def removefirst(self):
        if self.isempty():
            print("List is empty..")
            return
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.isempty():
            self._tail = None
        return e

    def removelast(self):
        if self.isempty():
            print("List is empty..")
            return
        e = self._tail._element
        self._tail = self._tail._prev 
        self._tail._next = None
        self._size -= 1
        return e

    def removeany(self, position):
        p = self._head
        count = 1
        while count < position-1:
            p = p._next
            count += 1
        e = p._next._element
        p._next = p._next._next
        p._next._prev = p
        self._size -= 1
        return e

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
        p = self._head
        while p:
            print(p._element, end=', ')
            p = p._next
        print()

    def displayrev(self):
        p = self._tail
        while p:
            print(p._element, end=', ')
            p = p._prev
        print()

obj = DoublyLinkedList()
obj.addlast(4)
obj.addlast(6)
obj.addlast(8)
obj.addlast(10)
obj.addlast(12)

obj.display()
obj.displayrev()
s = obj.__len__()
print("size:",s)

r = obj.search(12)
print("Index",r)