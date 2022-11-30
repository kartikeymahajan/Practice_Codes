package main

import "fmt"

type Stack []string

func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) Push(str string) {
	*s = append(*s, str)
}

func (s *Stack) Pop() (string, bool) {
	if s.IsEmpty() {
		return "", false
	} else {
		index := len(*s) - 1
		element := (*s)[index]
		*s = (*s)[:index]
		return element, true
	}
}

func main() {
	stack := Stack{}
	stack.Push("Two")
	stack.Push("Nine")
	stack.Push("Ten")
	stack.Push("Four")

	fmt.Println(stack)
	fmt.Println(len(stack))
	fmt.Println(stack.Pop())
	fmt.Println(stack)
	fmt.Println(len(stack))
	fmt.Println(stack.IsEmpty())

}
