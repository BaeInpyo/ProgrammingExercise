package main

import (
	"fmt"
	// "os"
)

const (
	inf = 2000000
)

var (
	edge    [1001][1001]int // 0 index is connecting to firetrucks
	cost    [1001]int
	visited [1001]bool

	nvertex int
	nedge   int
	nfire   int
	ntruck  int

	fire [1001]int
)

func initialize() {
	for x := 0; x <= nvertex; x++ {
		cost[x] = inf
		visited[x] = false
	}
	for x := 0; x <= nvertex; x++ {
		for y := 0; y <= nvertex; y++ {
			edge[x][y] = inf
		}
	}
}
func main() {
	//os.Stdin, _ = os.OpenFile("input.txt", os.O_RDONLY, 0644)
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d %d %d %d", &nvertex, &nedge, &nfire, &ntruck)
		initialize()

		for i := 1; i <= nedge; i++ {
			var a, b, d int
			fmt.Scanf("%d %d %d", &a, &b, &d)
			edge[a][b] = d
			edge[b][a] = d
		}

		for i := 0; i < nfire; i++ {
			fmt.Scanf("%d", &fire[i])
		}

		var t int
		for i := 0; i < ntruck; i++ {
			fmt.Scanf("%d", &t)
			edge[0][t] = 0
			edge[t][0] = 0
		}

		dijkstra(0)

		var result int = 0
		for i := 0; i < nfire; i++ {
			result += cost[fire[i]]
		}
		fmt.Printf("%d\n", result)
	}
}

func dijkstra(start int) { // start = 0
	var curr int = -1
	var next int = start
	cost[start] = 0

	for curr != next {
		curr = next
		visited[curr] = true
		// resolve
		min := inf
		for i := 1; i <= nvertex; i++ {
			if visited[i] == true {
				continue
			}
			if cost[i] > cost[curr]+edge[curr][i] {
				cost[i] = cost[curr] + edge[curr][i]
			}
			if min > cost[i] {
				min, next = cost[i], i
			}
		}
	}
}
