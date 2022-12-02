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
    # To remove nth node from last side of list.
    def remove(self, e):
        if self.isempty():
            print("List is empty..")
            return
        p = self._head
        x = self._size - e
        count = 0
        while count < x-1:
            p = p._next
            count += 1
        d = p._next._element
        p._next = p._next._next
        print(d,"deleted")

    def display(self):
        p = self._head
        while p:
            print(p._element, end=", ")
            p = p._next
        print()

    def rotateRight(self, head, k):
        if not head:
            return head

        #connect tail to head
        cur= self._head
        length =1
        while cur._next:
            cur = cur._next
            length+=1 
        cur._next = self._head

        #move to new head
        k= length - (k%length)
        while k>0:
            cur=cur._next
            k-=1

        #disconnect and return new head
        newhead = cur._next
        cur._next = None
        return newhead

obj = LinkedList()
obj.addlast(9)
obj.addlast(2)
obj.addlast(3)
obj.addlast(5)
obj.addlast(7)
obj.display()
obj.remove(1)
obj.display()
tp = obj
op = obj.rotateRight(tp, 2)
print(op)