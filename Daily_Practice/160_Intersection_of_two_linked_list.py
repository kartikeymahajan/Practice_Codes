# Compare two linked lists

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

    def delete(self, e):
        p = self._head
        if self.isEmpty():
            print("List is empty")
            return
        elif self._head._element == e:
            self._head = self._head._next
            self._size -=1
            return
        while p:
            if p._element == e:
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

    def isIdentical(self, list2):
        a = self._head
        b = list2._head
        while a and b:
            if a._element != b._element:
                return False
                
                # If we reach here, then a and b
                # are not null and their data is
                # same, so move to next nodes
                # in both lists

            a = a._next
            b = b._next

        # If linked lists are identical,
        # then 'a' and 'b' must be null
        # at this point.
        return (a == None and b == None)


list1 = LinkedList()
list2 = LinkedList()

list1.add(12)
list1.add(15)
list1.add(20)

list2.add(12)
list2.add(15)
list2.add(20)

list1.display()
print()
list2.display()

if list1.isIdentical(list2):
    print("Identical")
else:
    print("Not Identical")