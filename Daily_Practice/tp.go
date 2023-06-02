package main

import "fmt"

func countEven(num int) int {
	count := 0
	for i := 1; i <= num; i++ {
		temp := 0
		str_i := string(i)
		for j := 0; j < len(str_i); j++ {
			ss := string(str_i[j])
			temp += int(ss)
		}
		if temp%2 == 0 {
			count += 1
		}
	}
	return count
}

func main() {
	num := 30
	obj := countEven(num)
	fmt.Println(obj)
	// st := "kartikeya"
	// for i := 0; i < len(st); i++ {
	// 	fmt.Println(string(st[i]))
	// }
}
