package main

import "fmt"

func checkPalindrome(num int) bool {
	input_num := num
	var remainder int
	res := 0
	for num > 0 {
		remainder = num % 10
		fmt.Println(remainder)
		res = (res * 10) + remainder
		fmt.Println(res)
		num = num / 10
		fmt.Println(num)
	}

	if input_num == res {
		return true
	} else {
		return false
	}
}

func main() {
	fmt.Println(checkPalindrome(11))
}
