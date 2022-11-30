# Sort Linked List - Medium

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

    def display(self):
        p = self._head
        while p:
            print(p._element, end=", ")
            p = p._next
        print()

    def sort(self):
        current =  self._head
        index = None

        if self._head == None:
            return 
        else:
            while current:
                # Node index will point to node next to current
                index = current._next

                while index:
                    # if current nodes data is greater than index node data
                    # swap the data between them
                    if current._element > index._element:
                        temp = current._element
                        current._element = index._element
                        index._element = temp
                    index = index._next
                current = current._next

l = LinkedList()
l.add(32)
l.add(64)
l.add(68)
l.add(68)
l.add(9)
l.add(71)
l.display()
l.sort()
l.display()
