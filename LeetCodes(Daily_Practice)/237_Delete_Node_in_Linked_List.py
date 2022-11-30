# Delete Node in a Linked List  -   EASY

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

    def removeFirst(self):
        if self.isEmpty():
            print("List is empty")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -=1
        return e

    def removeLast(self):
        if self.isEmpty():
            print("List is empty")
            return
        p = self._head
        count = 1
        while count < self._size -1:
            p = p._next
            count += 1
        e = p._next._element
        p._next = None
        self._tail = p
        self._size -= 1

    def removeByIndex(self, i):
        p = self._head
        count = 0
        while count < i -1:
            p = p._next
            count += 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1

    def removeByElement(self, ele):
        p = self._head
        if self.isEmpty():
            print("List is empty")
            return
        elif self._head._element == ele:
            self._head = self._head._next
            self._size -=1
            return
        while p:
            if p._element == ele:
                break
            prev = p
            p = p._next
        if p == None:
            print("element Not found")
            return
        prev._next = p._next
        self._size -=1

    def display(self):
        p = self._head
        while p:
            print(p._element, end=", ")
            p = p._next
        print()

l = LinkedList()
l.add(2)
l.add(3)
l.add(5)
l.add(7)
l.display()
print(l.__len__())
l.removeByElement(5)
l.display()
print(l.__len__())