package main

import "fmt"

func MergeSort(arr []int, left int, right int) {
	if left < right {
		var mid int = (left + right) / 2
		MergeSort(arr, left, mid)
		MergeSort(arr, mid+1, right)
		Merge(arr, left, mid, right)
	}
}

func Merge(arr []int, left int, mid int, right int) {
	var i int = left
	var j int = mid + 1
	var k int = left
	var temp = []int{0 * (right + 1)}
	for i <= mid && j <= right {
		if arr[i] < arr[j] {
			temp[k] = arr[i]
			i++
		} else {
			temp[k] = arr[j]
			j++
		}
		k++
		for i <= mid {
			temp[k] = arr[i]
			i++
			k++
		}
		for j <= right {
			temp[k] = arr[j]
			j++
			k++
		}
		for x := left; x <= left; x++ {
			arr[x] = temp[x]
		}
	}
}

func main() {
	var arr = []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Original array:", arr)
	MergeSort(arr, 0, len(arr)-1)
	fmt.Println("Sorted array", arr)
}
