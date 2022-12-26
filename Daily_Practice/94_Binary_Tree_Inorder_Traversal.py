class Node:
    def __init__(self, element, left, right):
        self.element = element
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def makeTree(self, e, left, right):
        self.root = Node(e, left.root, right.root)

    def inOrder(self, troot):
        if troot:
            self.inOrder(troot.left)
            print(troot.element, end=" ")
            self.inOrder(troot.right)

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
empty = BinaryTree()
x.makeTree(2, empty, empty)
y.makeTree(3, empty, empty)
z.makeTree(1, x, y)
z.inOrder(z.root)

