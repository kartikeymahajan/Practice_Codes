package main

import "fmt"

func rob(slice []int) int {
	temp := 0
	if len(slice) == 2 {
		return 0
	} else {
		for i := 0; i < 2; i++ {
			count := 0
			for j := i; j < len(slice); j += 2 {
				count += slice[j]
			}
			if count > temp {
				temp = count
			}
		}
	}
	return temp
}

func main() {
	var nums = []int{1, 2, 1}
	obj := rob(nums)
	fmt.Println(obj)
}
