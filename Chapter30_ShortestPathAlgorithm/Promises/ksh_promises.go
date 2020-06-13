package main

import (
	"fmt"
	// "os"
)

const inf = 987654321

var (
	ncity  int
	nbuilt int
	nwill  int

	cost [201][201]int
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func initialize() {
	for a := 0; a < ncity; a++ {
		for b := 0; b < ncity; b++ {
			cost[a][b] = inf
		}
	}
}
func main() {
	// os.Stdin, _ = os.OpenFile("input.txt", os.O_RDONLY, 0644)
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d %d %d", &ncity, &nbuilt, &nwill)
		initialize()

		var a, b, c int
		for i := 0; i < nbuilt; i++ {
			fmt.Scanf("%d %d %d", &a, &b, &c)
			cost[a][b] = c
			cost[b][a] = c
		}
		floyd()

		result := 0
		for i := 0; i < nwill; i++ {
			fmt.Scanf("%d %d %d", &a, &b, &c)
			if update(a, b, c) == false {
				result++
			}
		}
		fmt.Println(result)
	}

}

func floyd() {
	for i := 0; i < ncity; i++ {
		cost[i][i] = 0
	}
	for k := 0; k < ncity; k++ {
		for a := 0; a < ncity; a++ {
			for b := 0; b < ncity; b++ {
				cost[a][b] = min(cost[a][b], cost[a][k]+cost[k][b])
			}
		}
	}
}

func update(a, b, c int) bool {
	if cost[a][b] <= c {
		return false
	}
	for x := 0; x < ncity; x++ {
		for y := 0; y < ncity; y++ {
			// x~a~b~y 또는 x~b~a~y 또는 x~y
			minimum := min(cost[x][a]+c+cost[b][y], cost[x][b]+c+cost[a][y])
			cost[x][y] = min(cost[x][y], minimum)
		}
	}
	return true
}
