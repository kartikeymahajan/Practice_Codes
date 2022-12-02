package main

import "fmt"

func BinarySearch(sl []int, element int) int {
	var l, r, m int
	l = 0
	r = len(sl) - 1
	for l <= r {
		m = (l + r) / 2
		if element == sl[m] {
			return m
		} else if element < sl[m] {
			r = m - 1
		} else if element > sl[m] {
			l = m + 1
		}
	}
	return -1
}

func main() {
	var sl = []int{12, 45, 65, 76, 83}
	op := BinarySearch(sl, 100)
	fmt.Println(op)
}
