package main

import (
	"fmt"
	// "os"
)

var (
	playerN  int           // max= 12
	matchN   int           // max = 100
	win      [12]int       // current win
	capacity [120][120]int // 120 >= 2(src+dst) + matchN + playerN
	flow     [120][120]int
	matches  [100][2]int

	bound int
	end   int
	src   int = 0
	dst   int = 1

	queue  [1000000]int
	qFront int
	qRear  int
)

func queueInit() {
	qFront = 0
	qRear = -1
}
func queueIsEmpty() bool {
	if qFront > qRear {
		return true
	}
	return false
}
func queuePop() int {
	item := queue[qFront]
	qFront++
	return item
}

func queuePush(item int) {
	qRear++
	queue[qRear] = item
}

func initialize() {
	for a := 0; a < end; a++ {
		for b := 0; b < end; b++ {
			capacity[a][b] = 0
			flow[a][b] = 0
		}
	}
}
func main() {
	// os.Stdin, _ = os.OpenFile("input.txt", os.O_RDONLY, 0644)
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d %d", &playerN, &matchN)

		bound = 2 + matchN
		end = 2 + matchN + playerN
		initialize()

		for i := 0; i < playerN; i++ {
			fmt.Scanf("%d", &win[i])
		}

		// 남은경기 인풋을 받으면서 0번이 최대로 이길수 있는 숫자를 체크
		maxAddVictory := 0
		for i := 0; i < matchN; i++ {
			fmt.Scanf("%d %d", &matches[i][0], &matches[i][1])
			if matches[i][0] == 0 || matches[i][1] == 0 {
				maxAddVictory++
			}
		}

		// make graph
		for i := 0; i < matchN; i++ {
			// src에서 각 경기로 가는 간선
			capacity[src][2+i] = 1
			flow[src][2+i] = 0
			// 각 경기에서 두 선수로 가는 간선
			for j := 0; j < 2; j++ {
				capacity[2+i][bound+matches[i][j]] = 1
				flow[2+i][bound+matches[i][j]] = 0
			}
		}

		// 각 선수에서 싱크로 가는 가능한 캐페서티
		capacity[bound+0][dst] = 0
		flow[bound+0][dst] = 0
		for i := 1; i < playerN; i++ {
			// 캐패서티 = 0번 선수의 현재 승점 -1 - x번선수의 승점
			capacity[bound+i][dst] = win[0] - 1 - win[i]
			flow[bound+i][dst] = 0
		}

		// capacity를 늘려가면서 확인
		// 1번조건은 자동으로 확인됨.
		result := -1
		totalflow := 0
		for addVictory := 0; addVictory <= maxAddVictory; addVictory++ {
			totalflow = networkFlow(src, dst, totalflow) // 현재 src, dst까지 보낼 수 있는 전체량

			if totalflow == matchN {
				result = win[0] + flow[bound+0][dst]
				break
			}

			// 모든 애들의 capacity를 하나씩 늘려준다.
			for i := 0; i < playerN; i++ {
				capacity[bound+i][dst]++
			}
		}
		fmt.Println(result)
	}
}

func networkFlow(src, dst, totalflow int) int {
	// 이미 캐패서티를 초과한 애가 잇으면 실패
	for i := 0; i < playerN; i++ {
		if capacity[bound+i][dst] < 0 {
			return totalflow
		}
	}

	for true {
		// bfs로 증가경로를 찾는다.

		var parent [120]int
		for i := 0; i < 120; i++ {
			parent[i] = -1
		}

		parent[src] = src
		queueInit()
		queuePush(src)

		for (queueIsEmpty() == false) && (parent[dst] == -1) {
			here := queuePop()
			for there := 0; there < end; there++ {
				if (capacity[here][there]-flow[here][there] > 0) && (parent[there] == -1) {
					queuePush(there)
					parent[there] = here
				}
			}
		}

		// 증가 경로가 없으면 종료
		if parent[dst] == -1 {
			break
		}

		// 증가경로를 통해 보낼 양 정하기
		amount := 87654321
		for p := dst; p != src; p = parent[p] {
			if capacity[parent[p]][p]-flow[parent[p]][p] < amount {
				amount = capacity[parent[p]][p] - flow[parent[p]][p]
			}
		}

		// 증가 경로를 통해 유량 보내기
		for p := dst; p != src; p = parent[p] {
			flow[parent[p]][p] += amount
			flow[p][parent[p]] -= amount
		}
		totalflow += amount
	}
	return totalflow
}
