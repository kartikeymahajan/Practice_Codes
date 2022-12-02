package main

import (
	"fmt"
)

func main() {
	rows := 15
	k := rows - 1
	for i := 0; i < rows; i++ {
		for j := 0; j < k; j++ {
			fmt.Print(" ")
		}
		k = k - 1
		for j := 0; j < i+1; j++ {
			fmt.Print("* ")
		}
		fmt.Println()
	}
}
