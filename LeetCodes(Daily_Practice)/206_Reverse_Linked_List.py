# Reverse Linked List  - Medium 

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

    def isEmpty(self):
        return self._size == 0

    def add(self, e):
        new = _Node(e, None)
        if self.isEmpty():
            self._head = new
            self._tail = new
        else:
            new._next = self._head
            self._head = new
        self._size += 1

    def reverse(self):
        prev = None
        current = self._head
        while current:
            self._next = current._next
            current._next = prev
            prev = current
            current = self._next
        self._head = prev 
        
    def display(self):
        p = self._head
        while p:
            print(p._element, end=", ")
            p = p._next
        print()

l = LinkedList()
l.add(5)
l.add(10)
l.add(20)
l.display()
l.reverse()
l.display()