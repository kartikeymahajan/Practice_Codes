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

    def SwapNodes(self, k, j):
        if self.isempty():
            print("List is empty..")
        a = self.search(k)
        count = 0
        p = self._head
        while count < a:
            p = p._next
            count+=1
        temp = p._element
        p._element = p._next._next._element
        p = p._next
        p._next._element = temp

obj = LinkedList()

obj.addlast(29)
obj.addlast(5)
obj.addlast(17)
obj.addlast(40)
obj.addlast(94)
obj.addlast(23)
obj.addlast(46)
obj.display()
obj.SwapNodes(17,94)
obj.display()