class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class DEQueLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addfirst(self, e):
        new = _Node(e, None)
        if self.isempty():
            self._head = new
            self._tail = new
        else:
            new._next = self._head
            self._head = new
        self._size +=1

    def addlast(self, e):
        new = _Node(e, None)
        if self.isempty():
            self._head = new
            self._tail = new
        else:
            self._tail._next = new
            self._tail = new
        self._size += 1

    def removefirst(self):
        if self.isempty():
            print("Deque is empty")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -=1
        if self.isempty():
            self._rear = None
        return e

    def removelast(self):
        if self.isempty():
            print("Deque is empty")
            return
        p = self._head
        count = 1
        while count < self.__len__() -1:
            p = p._next
            count +=1
        e = self._tail._element
        self._tail = p
        self._tail._next = None
        self._size -=1
        return e

    def first(self):
        if self.isempty():
            print("Deque is empty")
            return
        return self._head._element

    def last(self):
        if self.isempty():
            print("Deque is empty")
            return
        return self._tail._element

    def display(self):
        p = self._head
        while p:
            print(p._element, end=', ')
            p = p._next
        print()

d = DEQueLinkedList()

d.addlast(4)
d.addlast(6)
d.addlast(8)

d.display()
print("Length:",d.__len__())

d.addfirst(2)
d.display()
print("Length:",d.__len__())

print("First:",d.first())
print("Last:", d.last())

print("Item Removed", d.removefirst())
d.display()
print("Length:",d.__len__())

print("Item removed",d.removelast())
d.display()
print("Length:",d.__len__())

print("isempty?",d.isempty())

