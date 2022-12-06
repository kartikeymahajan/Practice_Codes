package main

import (
	"fmt"
)

func plusOne(digits []int) []int {
	c := 1
	for i := len(digits) - 1; i >= 0; i-- {
		s := digits[i] + c
		digits[i] = s % 10
		c = s / 10
	}
	if c > 0 {
		return append([]int{1}, digits...)
	} else {
		return digits
	}
}

func main() {
	var sl = []int{1, 2, 3}
	op := plusOne(sl)
	fmt.Println(op)
}
