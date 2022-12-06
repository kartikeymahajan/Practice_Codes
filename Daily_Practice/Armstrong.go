package main

import "fmt"

func main() {
	var num, sum, temp, digit int

	num = 159
	sum = 0
	temp = num
	for temp > 0 {
		digit = temp % 10
		sum = sum + digit*digit*digit
		temp = temp / 10
	}

	if num == sum {
		fmt.Println(num, "is an armstrong number")
	} else {
		fmt.Println(num, "is not an armstrong number")
	}
}
