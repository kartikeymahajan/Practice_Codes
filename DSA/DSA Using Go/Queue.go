package main

import (
	"fmt"
	"sort"
)

type Queue []string

func (q *Queue) IsEmpty() bool {
	return len(*q) == 0
}

func (q *Queue) Enqueue(str string) {
	*q = append(*q, str)
}

func (q *Queue) Dequeue() (string, bool) {
	if q.IsEmpty() {
		return "", false
	} else {
		element := (*q)[0]
		*q = (*q)[1:]
		return element, true
	}
}

func (q *Queue) Sorting() []string {
	sort.Strings(*q)
	return *q

}

func main() {
	queue := Queue{}
	queue.Enqueue("I")
	queue.Enqueue("Love")
	queue.Enqueue("You")
	queue.Enqueue("Dear")

	fmt.Println(queue)
	fmt.Println(len(queue))
	fmt.Println(queue.Dequeue())
	fmt.Println(queue)
	fmt.Println(len(queue))
	fmt.Println(queue.Sorting())
}
