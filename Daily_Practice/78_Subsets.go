package main

import "fmt"

func subsets(nums []int) [][]int {
	return helper(nums, 0)
}

func helper(nums []int, p int) [][]int {
	var result [][]int
	result = append(result, []int{})
	if p == len(nums) {
		return result
	}

	for i := p; i < len(nums); i++ {
		temp := helper(nums, i+1)
		for j := range temp {
			t := append([]int{nums[i]}, temp[j]...)
			result = append(result, t)
		}
	}

	return result
}
func main() {
	var nums = []int{1, 2, 3, 4}
	obj := subsets(nums)
	fmt.Println(obj)
}
