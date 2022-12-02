# Delete duplicate-value nodes from a sorted linked list  - EASY

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

    def removeDuplicates(self):
        p = self._head
        if p is None:
            return
        while p._next is not None:
            if p._element == p._next._element:
                new = p._next._next
                p._next = None
                p._next = new
                self._size -= 1
            else:
                p = p._next
        return self._head

    # def removeDuplicates(self):
    #     # Node p will point to head 
    #     p = self._head
    #     index = None
    #     temp = None

    #     if self._head == None:
    #         return
    #     else:
    #         while p:
    #             #Node temp will point to previous node to index. 
    #             temp = p
    #             #Index will point to node next to p  
    #             index = p._next

    #             while index:
    #                 #If current node's data is equal to index node's data 
    #                 if p._element == index._element:
    #                     #Here, index node is pointing to the node which is duplicate of current node  
    #                     #Skips the duplicate node by pointing to next node  
    #                     temp._next = index._next
    #                 else:
    #                     #Temp will point to previous node of index.  
    #                     temp = index
    #                 index = index._next
    #             p = p._next


l = LinkedList()
l.add(15)
l.add(15)
l.add(15)
l.add(10)
l.add(10)
l.add(5)
l.display()
print(l.__len__())
l.removeDuplicates()
l.display()
print(l.__len__())

                    