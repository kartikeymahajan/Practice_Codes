package main

import "fmt"

func minPathSum(grid [][]int) int {
	output := 0

	for _, i := range grid {
		for _, j := range i {
			output += j
		}
		break
	}

	for i := len(grid) - 1; i > 0; i-- {
		var temp = [][]int{grid[i]}
		for j := len(temp[0]) - 1; j > len(temp[0])-2; j-- {
			output += temp[0][j]
		}
	}
	return output
}

func main() {
	var grid = [][]int{{10, 20}, {10, 40}, {10, 30}}
	op := minPathSum(grid)
	fmt.Println(op)
}
