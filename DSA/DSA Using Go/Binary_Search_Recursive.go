package main

import (
	"fmt"
)

func BinarySearch(slice []int, element, left, right int) int {
	var m int
	if left > right {
		return -1
	} else {
		m = (left + right) / 2
		if slice[m] == element {
			return m
		} else if element < slice[m] {
			return BinarySearch(slice, element, left, m-1)
		} else if element > slice[m] {
			return BinarySearch(slice, element, m+1, right)
		}
	}
	return -1
}

func main() {
	var slice = []int{12, 45, 65, 76, 83}
	op := BinarySearch(slice, 100, 0, len(slice)-1)
	fmt.Println(op)
}
