package main

import "fmt"

type inputType struct {
	command int
	a       int
	b       int
}

const (
	ackType = 0
	disType = 1
)

var (
	belongsTo [10000]int
	dislike   [10000]int
	height    [10000]int
	weight    [10000]int
	n, m      int
	input     [100001]inputType
)

func initialize() {
	for i := 0; i < n; i++ {
		belongsTo[i] = i
		dislike[i] = -1
		height[i] = 1
		weight[i] = 1
	}
}

func find(a int) int {
	if a == -1 {
		return -1
	}
	for a != belongsTo[a] {
		a = belongsTo[a]
	}
	return a
}
func union(a int, b int) int {
	if a == -1 || b == -1 {
		if a < b {
			return b
		}
		return a
	}
	pa := find(a)
	pb := find(b)
	if pa == pb {
		return pa
	}
	if height[pa] < height[pb] {
		temp := pa
		pa = pb
		pb = temp
	} // pa >= pb

	if height[pa] == height[pb] {
		height[pa]++
	}
	belongsTo[pb] = pa
	weight[pa] += weight[pb]
	return pa

}

func ack(a int, b int) bool {
	pa := find(a)
	pb := find(b)

	if dislike[pa] == pb {
		return false
	}

	pp := union(pa, pb)

	dd := union(dislike[pa], dislike[pb])
	dislike[pp] = dd
	if dd != -1 {
		dislike[dd] = pp
	}
	return true
}

func dis(a int, b int) bool {
	pa := find(a)
	pb := find(b)
	if pa == pb {
		return false
	}
	na := union(pa, dislike[pb])
	nb := union(pb, dislike[pa])
	dislike[na] = nb
	dislike[nb] = na
	return true
}
func solution() int {
	var idx int
	for idx = 1; idx <= m; idx++ {
		var ok bool
		if input[idx].command == ackType {
			ok = ack(input[idx].a, input[idx].b)
		} else {
			ok = dis(input[idx].a, input[idx].b)
		}
		if ok == false {
			break
		}
	}
	return idx
}

func calcMax() int {
	var result int = 0
	for i := 0; i < n; i++ {
		if find(i) == i { // 루트인 애들에 대해서만 보면 됨
			enemy := dislike[i]
			if enemy > i {
				continue
			}
			myWeight := weight[i]
			enemyWeight := 0
			if enemy != -1 {
				enemyWeight = weight[enemy]
			}
			if myWeight > enemyWeight {
				result += myWeight
			} else {
				result += enemyWeight
			}
		}
	}

	return result
}
func main() {
	//stdin, _ := os.OpenFile("input.txt", os.O_RDONLY, 0666)
	//os.Stdin = stdin
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d %d", &n, &m)
		initialize()
		var comment string
		for idx := 1; idx <= m; idx++ {
			fmt.Scanf("%s %d %d", &comment, &input[idx].a, &input[idx].b)
			if comment == "ACK" {
				input[idx].command = ackType
			} else {
				input[idx].command = disType
			}
		}
		result := solution()
		if result <= m {
			fmt.Printf("CONTRADICTION AT %d\n", result)
		} else {
			fmt.Printf("MAX PARTY SIZE IS %d\n", calcMax())
		}
	}
}

