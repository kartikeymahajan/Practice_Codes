package main

import "fmt"

func BubbleSort(slice []int) {
	n := len(slice)
	for pass := n - 1; pass >= 0; pass-- {
		for i := 0; i < pass; i++ {
			if slice[i] > slice[i+1] {
				temp := slice[i]
				slice[i] = slice[i+1]
				slice[i+1] = temp
			}
		}
	}
}

func main() {
	var slice = []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Slice before sorting:", slice)
	BubbleSort(slice)
	fmt.Println("Slice after sorting:", slice)
}
