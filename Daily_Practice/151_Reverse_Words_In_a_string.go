package main

import (
	"fmt"
	"strings"
)

func ReverseWords(st string) string {
	sl := strings.Split(st, " ")
	var reverse = []string{}
	for i := len(sl) - 1; i >= 0; i-- {
		reverse = append(reverse, sl[i])
	}
	output := strings.Join(reverse, " ")
	return output
}

func main() {
	st := "My name is kartik"
	op := ReverseWords(st)
	fmt.Println(op)
}
