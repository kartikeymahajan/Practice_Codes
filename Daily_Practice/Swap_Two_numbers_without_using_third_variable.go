package main

import "fmt"

func main() {
	var num1 = 10
	var num2 = 20

	fmt.Printf("Before Swapping num1 = %d & num2 = %d\n", num1, num2)

	num1 = num1 - num2
	num2 = num1 + num2
	num1 = num2 - num1

	fmt.Printf("After Swapping num1 = %d & num2 = %d", num1, num2)
}
