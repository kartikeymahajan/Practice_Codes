from QueuesLinkedList import QueuesLinkedList

class _Node:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def makeTree(self,e, left, right):
        self.root = _Node(e, left.root, right.root)

    def inorder(self, troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element, end=" ")
            self.inorder(troot.right)

    def preorder(self, troot):
        if troot:
            print(troot.element, end=" ")
            self.preorder(troot.left)
            self.preorder(troot.right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element, end=" ")

    def levelorder(self):
        q = QueuesLinkedList()
        present = self.root
        print(present.element, end=" ")
        q.enqueue(present)
        while not q.isempty():
            present = q.dequeue()
            if present.left:
                print(present.left.element, end=" ")
                q.enqueue(present.left)
            if present.right:
                print(present.right.element, end=" ")
                q.enqueue(present.right)



x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
empty = BinaryTree()
x.makeTree(60, empty, empty)
y.makeTree(50, empty, x)
z.makeTree(40, empty, empty)
r.makeTree(30, y, empty)
s.makeTree(20, z, empty)
t.makeTree(10, s, r)
print("\nInorder Traversal")
t.inorder(t.root)
print("\nPreorder Traversal")
t.preorder(t.root)
print("\nPostorder Traversal")
t.postorder(t.root)
print("\nLevelorder Traversal")
t.levelorder()