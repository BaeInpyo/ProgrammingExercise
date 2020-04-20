package main

import (
	"fmt"
	// "os"
)

const (
	unwatched int = 0
	watched   int = 1
	installed int = 2
)

var (
	n      int
	g      int
	result int

	visited [1000]bool
	edge    [1000][1000]int
	edgeN   [1000]int
)

func initialize() {
	for i := 0; i < n; i++ {
		visited[i] = false
		edgeN[i] = 0
	}
	result = 0
}

func main() {
	// os.Stdin, _ = os.OpenFile("input.txt", os.O_RDONLY, 0644)
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		initialize()

		fmt.Scanf("%d %d", &n, &g)

		// make graph
		var a, b int
		for i := 0; i < g; i++ {
			fmt.Scanf("%d %d", &a, &b)
			edge[a][edgeN[a]] = b
			edge[b][edgeN[b]] = a
			edgeN[a]++
			edgeN[b]++
		}

		// check with dfs
		for i := 0; i < n; i++ {
			if !visited[i] {
				dfs(i)
			}
		}
		fmt.Printf("%d\n", result)
	}
}

func dfs(curr int) int {
	visited[curr] = true
	// dfs를 타고 계속 내려가자. 이러면 자동으로 dfs 트리 깊은 곳에서부터 차근차근 올라올수 있음...

	// 만약 내가 리프노드인경우에는 그냥 설치 안해야함 (그래프가 한개짜리 vertex이면 install)
	// 그리고 내 자식들 중에 하나라도 unwatched 이면 설치해야하고
	// 나머지는 전부 watched ??

	// 아래가 watched밖에 없으면 설치해야하고

	var isLeaf bool = true
	var isRoot bool = true
	var countUnwatched int = 0
	var countInstalled int = 0

	for i := 0; i < edgeN[curr]; i++ {
		next := edge[curr][i]
		if visited[next] {
			isRoot = false
		} else {
			// visited가 false인 경우에만 curr의 자식
			isLeaf = false
			state := dfs(next)
			if state == unwatched {
				countUnwatched++
			}
			if state == installed {
				countInstalled++
			}
		}
	}

	if isRoot && isLeaf { // only 1 vertex in graph
		result++
		return installed
	}
	if isLeaf { // leaf node
		return unwatched
	}

	if countUnwatched > 0 { // 자식중에 하나라도 unwatched이면 설치
		result++
		return installed
	}
	if countInstalled > 0 { // 자식중에 이미 설치가 되어있으면 watched
		return watched
	}
	if isRoot { // 여기까지 왔으면 자식들이 모두 watched인데, 내가 root이면 installed
		result++
		return installed
	}
	return unwatched
}

/*
3
2
999
3
3
3
*/
