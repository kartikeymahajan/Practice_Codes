package main

import (
	"fmt"
)

func findMaxElement(arr []int) int {
	max_num := arr[0]
	for i := 0; i < len(arr); i++ {
		if arr[i] > max_num {
			max_num = arr[i]
		}
	}
	return max_num
}

func CountSort(arr []int) {
	n := len(arr)
	maxsize := findMaxElement(arr)
	var carray = []int{0 * (maxsize + 1)}
	for i := 0; i < n; i++ {
		carray[arr[i]] = carray[arr[i]] + 1
	}
	var i, j = 0, 0
	for i < maxsize+1 {
		if carray[i] > 0 {
			arr[j] = i
			j++
			carray[i] = carray[i] - 1
		} else {
			i++
		}
	}
}

func main() {
	var arr = []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Original Array:", arr)
	CountSort(arr)
	fmt.Println("Sorted Array:", arr)
}
