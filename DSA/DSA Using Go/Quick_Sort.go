package main

import "fmt"

func QuickSort(arr []int, low int, high int) {
	if low < high {
		pi := Partision(arr, low, high)
		QuickSort(arr, low, pi-1)
		QuickSort(arr, pi+1, high)
	}
}

func Partision(arr []int, low int, high int) int {
	pivot := arr[low]
	i := low + 1
	j := high
	for true {
		for i <= j && arr[i] <= pivot {
			i++
		}
		for i <= j && arr[j] > pivot {
			j--
		}
		if i <= j {
			temp := arr[i]
			arr[i] = arr[j]
			arr[j] = temp
		} else {
			break
		}

	}
	temp := arr[low]
	arr[low] = arr[j]
	arr[j] = temp
	return j
}

func main() {
	var arr = []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Original array:", arr)
	QuickSort(arr, 0, len(arr)-1)
	fmt.Println("Sorted array", arr)
}
