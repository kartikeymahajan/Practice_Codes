package main

import "fmt"

func InsertionSort(slice []int) {
	n := len(slice)
	for i := 1; i < n; i++ {
		cvalue := slice[i]
		position := i
		for position > 0 && slice[position-1] > cvalue {
			slice[position] = slice[position-1]
			position = position - 1
		}
		slice[position] = cvalue
	}
}

func main() {
	var slice = []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Slice before sorting:", slice)
	InsertionSort(slice)
	fmt.Println("Slice after sorting:", slice)
}
