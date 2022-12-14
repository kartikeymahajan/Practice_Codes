package main

import "fmt"

type node struct {
	data int
	next *node
}

type linkedList struct {
	head   *node
	tail   *node
	length int
}

func (l *linkedList) _len() int {
	return l.length
}

func (l *linkedList) addLast(value int) {
	newNode := node{data: value}
	if l.head == nil {
		l.head = &newNode
		l.tail = &newNode
	} else {
		l.tail.next = &newNode
		l.tail = &newNode
	}
	l.length++
}

func (l *linkedList) printList() {
	if l.head == nil {
		return
	}
	currentNode := l.head
	for currentNode != nil {
		fmt.Print(currentNode.data, ", ")
		currentNode = currentNode.next
	}
	fmt.Println()
}

func (l *linkedList) SwapNodes()

func main() {
	myList := linkedList{}
	myList.addLast(12)
	myList.addLast(15)
	myList.addLast(57)
	myList.addLast(89)
	myList.addLast(100)
	myList.printList()
	op := myList._len()
	fmt.Println(op)
}
