package main

import "fmt"

type node struct {
	data int
	next *node
}

type linkedList struct {
	head   *node
	length int
}

func (l *linkedList) len() {
	fmt.Println("Size of list ", l.length)
}

func (l *linkedList) prepend(value int) {
	newNode := node{data: value}
	if l.head == nil {
		l.head = &newNode
		l.length++
	} else {
		newNode.next = l.head
		l.head = &newNode
		l.length++
	}
	return
}

func (l *linkedList) printList() {
	if l.head == nil {
		return
	}

	currentNode := l.head
	for currentNode != nil {
		fmt.Println(currentNode.data)
		currentNode = currentNode.next
	}
}

func (l *linkedList) deleteWithValue(value int) {
	if l.length == 0 {
		fmt.Println("List is empty")
		return
	}

	if l.head.data == value {
		l.head = l.head.next
		l.length--
		fmt.Printf("%d delted", value)
		return
	}

	previousToDelete := l.head
	for previousToDelete.next.data != value {
		if previousToDelete.next.next == nil {
			fmt.Println("value not found")
			return
		}
		previousToDelete = previousToDelete.next
	}
	previousToDelete.next = previousToDelete.next.next
	fmt.Printf("%d deleted\n", value)
	l.length--
}

func main() {
	myList := linkedList{}
	myList.prepend(12)
	myList.prepend(24)
	myList.prepend(36)
	myList.printList()
	fmt.Println()
	myList.deleteWithValue(12)
	myList.printList()
	myList.len()
}
