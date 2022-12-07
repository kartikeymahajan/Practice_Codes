package main

import "fmt"

func ShellSort(slice []int) {
	var n, gap, i, temp, j int
	n = len(slice)
	gap = n / 2
	for gap > 0 {
		i = gap
		for i < n {
			temp = slice[i]
			j = i - gap
			for j >= 0 && slice[j] > temp {
				slice[j+gap] = slice[j]
				j = j - gap
			}
			slice[j+gap] = temp
			i++
		}
		gap = gap / 2
	}
}

func main() {
	var slice = []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Before sorting:", slice)
	ShellSort(slice)
	fmt.Println("After sorting:", slice)
}
