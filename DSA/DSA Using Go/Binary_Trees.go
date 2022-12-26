package main

import "fmt"

type Node struct {
	Data  int
	Left  *Node
	Right *Node
}

func CreateNode(v int) *Node {
	return &Node{v, nil, nil}
}

func (root *Node) GetTreeNodeNum() int {
	if root == nil {
		return 0
	} else {
		// calculate the number of nodes under the left node
		// calculate the number of nodes under the right node
		// and finally add the number of root nodes.
		return root.Left.GetTreeNodeNum() + root.Right.GetTreeNodeNum() + 1
	}
}

func (root *Node) GetTreeDegree() int {
	maxDegree := 0

	if root == nil {
		return maxDegree
	}

	if root.Left.GetTreeDegree() > root.Right.GetTreeDegree() {
		maxDegree = root.Left.GetTreeDegree()
	} else {
		maxDegree = root.Right.GetTreeDegree()
	}

	return maxDegree + 1
}

func (root *Node) PreOrder() {
	if root != nil {
		// print root
		fmt.Print(root.Data, " ")
		// print left tree
		root.Left.PreOrder()
		// print right tree
		root.Right.PreOrder()
	}
}

func (root *Node) PostOrder() {
	if root != nil {
		// print left tree
		root.Left.PostOrder()
		// print right tree
		root.Right.PostOrder()
		// print root
		fmt.Print(root.Data, " ")
	}
}

func (root *Node) InOrder() {
	if root != nil {
		// print left tree
		root.Left.InOrder()
		// print root
		fmt.Print(root.Data, " ")
		// print right tree
		root.Right.InOrder()
	}
}

func InitTree() *Node {
	root := CreateNode(1)           //root node
	root.Left = CreateNode(2)       //left subtree
	root.Right = CreateNode(3)      //right subtree
	root.Left.Left = CreateNode(4)  //right subtree of left subtree
	root.Left.Right = CreateNode(5) //left subtree of the left subtree of the right subtree
	root.Right.Left = CreateNode(6)
	root.Right.Right = CreateNode(7)
	return root
}

func main() {
	obj := InitTree()
	fmt.Println("Preorder Traversal")
	obj.PreOrder()
	fmt.Println()
	fmt.Println("Inorder Traversal")
	obj.InOrder()
	fmt.Println()
	fmt.Println("Postorder Traversal")
	obj.PostOrder()
}
