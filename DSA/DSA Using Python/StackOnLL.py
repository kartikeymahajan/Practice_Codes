class _Node:
    __spots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class StackOnLinkedList:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, e):
        new = _Node(e, None)
        if self.isempty():
            self._top = new
        else:
            new._next = self._top
            self._top = new
        self._size +=1

    def pop(self):
        if self.isempty():
            print("List is empty")
            return
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def top(self):
        if self.isempty():
            print("List is empty")
            return
        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element,end=', ')
            p = p._next
        print()

l = StackOnLinkedList()
l.push(23)
l.push(45)
l.push(78)
l.push(89)
l.display()
print("Size:",l.__len__())

print(l.pop())
l.display()
print("Size:",l.__len__())

print(l.top())


        