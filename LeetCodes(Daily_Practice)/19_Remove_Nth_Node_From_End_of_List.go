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

func (l *linkedList) len() {
	fmt.Println("Size of list ", l.length)
}

func (l *linkedList) addlast(value int) {
	newNode := node{data: value}
	p := l.head
	count := 0
	if l.head == nil {
		l.head = &newNode

	} else {
		for count < l.length-1 {
			p = p.next
			count++
		}
		p.next = &newNode
	}
	l.tail = &newNode
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

// Removing given positions element from lastside of Linkedlist.
func (l *linkedList) removeElement(position int) {
	if l.head == nil {
		return
	}
	x := l.length - position
	p := l.head
	count := 0

	for count < x-1 {
		p = p.next
		count++
	}
	ele := p.next.data
	p.next = p.next.next
	l.length--
	fmt.Println(ele, "deleted")
}

func main() {
	myList := linkedList{}
	myList.addlast(89)
	myList.addlast(100)
	myList.addlast(201)
	myList.addlast(488)
	myList.addlast(167)
	myList.addlast(983)
	myList.printList()
	myList.len()
	myList.removeElement(4)
	myList.printList()
	myList.len()
}
