package main

import "fmt"

func findIndex(sl []int, element int) int {
	index := 0
	for index < len(sl) {
		if sl[index] == element {
			return index
		}
		index++
	}
	return -1
}

func main() {
	var sl = []int{23, 45, 56, 14, 52}
	op := findIndex(sl, 90)
	fmt.Println(op)
}
