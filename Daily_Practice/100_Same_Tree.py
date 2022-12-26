# Pending..................................................................



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

    def preOrder(self, troot):
        if troot:
            Tree.append(troot.element)
            self.preOrder(troot.left)
            self.preOrder(troot.right)
        return Tree

    # def isSameTree(self,p,q):
    #     if p == q:
    #         return True
    #     else:
    #         return False

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #if Both are null then return True
        if(p == None and q == None):
            return True
        # if one of them is null then of course tree are not same hence return False
        if(p == None or q == None):
            return False
        # Classic case of preOrder Traversal, check curr values and then go left check and then go right check 
        return p.element == q.element and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


Tree = []
# TreeOne
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
empty = BinaryTree()
x.makeTree(2, empty, empty)
y.makeTree(3, empty, empty)
z.makeTree(1, x, y)
obj1 = z.preOrder(z.root)

Tree.clear()


#TreeTwo
a = BinaryTree()
b = BinaryTree()
c = BinaryTree()
empty = BinaryTree()
a.makeTree(2, empty, empty)
b.makeTree(3, empty, empty)
c.makeTree(5, x, y)
obj2 = c.preOrder(c.root)

print("obj1",obj1)
print("obj2",obj2)

temp = BinaryTree().isSameTree(z,c)
print(temp)




