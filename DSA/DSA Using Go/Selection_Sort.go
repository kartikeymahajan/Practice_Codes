package main

import "fmt"

func SelectionSort(slice []int) []int {
	n := len(slice)
	for i := 0; i < n-1; i++ {
		position := i
		for j := i + 1; j < n; j++ {
			if slice[j] < slice[position] {
				position = j
			}
		}
		temp := slice[i]
		slice[i] = slice[position]
		slice[position] = temp
	}
	return slice
}

func main() {
	var slice = []int{23, 5, 36, 74, 13, 74, 93, 23, 56, 82, 45}
	op := SelectionSort(slice)
	fmt.Println(op)
}
