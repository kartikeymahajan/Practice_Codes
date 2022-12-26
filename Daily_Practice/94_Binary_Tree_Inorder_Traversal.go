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

/*
Tree representation--
          1
        /   \
	   2     3
	  / \   / \
     4   5 6   7

*/

func main() {
	obj := InitTree()
	obj.InOrder()
}
