package main

import (
	"fmt"
	"os"
)

type treeNode struct {
	ancestor [18]int // 2^17 = 124*1024
	depth    int
}

var (
	n, pairN int
	a, b     int
	node     [100000]treeNode
)

func initialize(treenode *treeNode) {
	for i := 0; i < 18; i++ {
		treenode.ancestor[i] = -1
	}
	treenode.depth = 0
}
func main() {
	stdin, _ := os.OpenFile("input.txt", os.O_RDONLY, 0666)
	os.Stdin = stdin

	var testcase int
	fmt.Scanf("%d", &testcase)

	node[0].ancestor[0] = -1
	initialize(&node[0])
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d %d", &n, &pairN)

		for i := 1; i < n; i++ {
			initialize(&node[i])
			fmt.Scanf("%d", &node[i].ancestor[0])
			// ancestor[0].ancestor[0]이 나의 ancestor[1]이고
			// ancestor[1].ancestor[1]이 나의 ancestor[2]이고
			// ...
			parent := node[i].ancestor[0]
			node[i].depth = node[parent].depth + 1
			step := 1
			for parent >= 0 {
				node[i].ancestor[step] = node[parent].ancestor[step-1]
				parent = node[i].ancestor[step]
				step++
			}
		}
		for i := 0; i < pairN; i++ {
			fmt.Scanf("%d %d", &a, &b)
			result := lca(a, b)
			fmt.Println(result)
		}

	}

}

func lca(a int, b int) int {
	count := 0
	// make common depth

	// make depth a >= b
	if node[a].depth < node[b].depth {
		temp := a
		a = b
		b = temp
	}
	//make common depth
	for true {
		if node[a].depth == node[b].depth {
			break
		}
		var nextIdx int = a
		for step := 0; step < 18; step++ {
			ancestor := node[a].ancestor[step]
			// a의 depth가 b보다 낮아지거나 없어지기 전까지...
			if ancestor < 0 || node[ancestor].depth < node[b].depth {
				break
			}
			nextIdx = ancestor
		}
		count += node[a].depth - node[nextIdx].depth
		a = nextIdx
	}

	// find lca
	for a != b {
		nextStep := 0
		for step := 0; step < 18; step++ {
			// 두 조상이 같기 전까지 계속해서 증가시킨다.
			if node[a].ancestor[step] == node[b].ancestor[step] {
				break
			}
			nextStep = step
		}
		a = node[a].ancestor[nextStep]
		count += 2 * (node[b].depth - node[a].depth)
		b = node[b].ancestor[nextStep]
	}

	return count
}

// 음... 이거 lca 그.. 바이너리서치하듯이 못하네
// 인풋중에 순서가 뒤바껴서 들어오는 경우가 잇는것 같다.
