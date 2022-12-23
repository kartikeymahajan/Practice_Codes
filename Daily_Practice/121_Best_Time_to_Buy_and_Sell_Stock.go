package main

import (
	"fmt"
)

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	smallest := prices[0]
	max_profit := 0
	for _, elem := range prices {
		if elem < smallest {
			smallest = elem
		} else {
			if max_profit > elem-smallest {
				max_profit = max_profit
			} else {
				max_profit = elem - smallest
			}
		}
	}
	return max_profit
}

func main() {
	var prices = []int{5, 3, 6, 2}
	obj := maxProfit(prices)
	fmt.Println(obj)
}
