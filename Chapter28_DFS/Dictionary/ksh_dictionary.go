package main

import (
	"fmt"
	"os"
)

var (
	n       int
	input   [1000]string
	result  [26]int
	resultN int
	visited [26]bool
	edge    [26][26]bool
)

// 쭉 관계 그래프 그리고
// dfs로 마지막 방문한 노드들 죽 추가해주고
// 뒤에서부터 출력
func toNumber(cha byte) int {
	return int(cha - 'a')
}
func toByte(i int) byte {
	return byte(i + 'a')
}
func initialize() {
	for a := 0; a < 26; a++ {
		for b := 0; b < 26; b++ {
			edge[a][b] = false
		}
		visited[a] = false
	}
	resultN = 0
}

func main() {
	os.Stdin, _ = os.OpenFile("input.txt", os.O_RDONLY, 0666)
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		initialize()
		fmt.Scanf("%d", &n)
		for i := 0; i < n; i++ {
			fmt.Scanf("%s", &input[i])
		}

		makeGraph()

		for i := 0; i < 26; i++ {
			dfs(i)
		}

		impossible := false
		// 현재 result[]에는 a ... b ... ( b --> a 로 딕셔너리 순서임. 즉, a -> b로 가는 순서가 있으면 안됨)
		for fi := 0; fi < 26; fi++ {
			front := result[fi]
			for ri := fi + 1; ri < 26; ri++ {
				rear := result[ri]
				if edge[front][rear] {
					impossible = true
					break
				}
			}
			if impossible {
				break
			}
		}
		if impossible {
			fmt.Printf("INVALID HYPOTHESIS")
		} else {
			for i := 26 - 1; i >= 0; i-- {
				fmt.Printf("%c", toByte(result[i]))
			}
		}
		fmt.Printf("\n")

	}
}

func makeGraph() {
	for i := 0; i < n-1; i++ {
		front, rear := findDifferentIdx(input[i], input[i+1])
		if front == 0 {
			continue
		}
		// front alpabet -> rear alphabet
		edge[toNumber(front)][toNumber(rear)] = true
	}
}

func findDifferentIdx(front string, rear string) (byte, byte) {
	var i int
	for i = 0; i < len(front); i++ {
		if front[i] != rear[i] {
			break
		}
	}
	if i == len(front) {
		return 0, rear[i]
	}
	return front[i], rear[i]
}

func dfs(curr int) {
	if visited[curr] {
		return
	}
	visited[curr] = true
	for i := 0; i < 26; i++ {
		if edge[curr][i] {
			dfs(i)
		}
	}
	result[resultN] = curr
	resultN++
}
