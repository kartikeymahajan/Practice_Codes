package main

import "fmt"

func Fabonacci(num int) {
	var n1, n2 = 0, 1
	var nth int
	if num <= 0 {
		fmt.Println("Please enter a positive number...")
	} else if num == 1 {
		fmt.Println(n1)
	} else if num > 1 {
		fmt.Print("Fabonacci Sequence:", " ")
		for i := 0; i < num; i++ {
			fmt.Print(n1, ", ")
			nth = n1 + n2
			n1 = n2
			n2 = nth
		}
	}
}

func main() {
	Fabonacci(10)
}
