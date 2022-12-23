package main

import "fmt"

func hammingWeight(num uint32) int {
	res := 0
	for i := 0; i < 32; i++ {
		res += int((num >> 31) & 1)
		num <<= 1
	}
	return res
}

func main() {
	op := hammingWeight(00000000000000000000000000001011)
	fmt.Println(op)
}
