
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class QueuesLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def enqueue(self, e):
        new = _Node(e, None)
        if self.isempty():
            self._head = new
            self._tail = new
        else:
            self._tail._next = new
            self._tail = new
        self._size += 1

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        return e

    def first(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self._head._element

    def display(self):
        p = self._head
        while p:
            print(p._element,end=', ')
            p = p._next
        print()


q = QueuesLinkedList()
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)

q.display()
print("Length:",q.__len__())

print("Item Removed:",q.dequeue())
q.display()
print("Length:",q.__len__())

print("First element:",q.first())
