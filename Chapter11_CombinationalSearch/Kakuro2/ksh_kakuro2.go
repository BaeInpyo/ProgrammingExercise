//
// 아 이거.... block의 direction을 나눠줘야함.. 내가 이걸 통일로해버림..
//
package main

import (
	"fmt"
	"os"
)

const (
	maxN int = 20

	horizontal int = 0
	vertical   int = 1

	black int = 0
	white int = 1
	hint  int = 2

	notDefined int = 0
	allBit     int = 1022 // 1111111110 (2)

)

type block struct {
	color int

	// for white
	value int // 0: not defined, 1~9
	bit   int // number can be inserted, ex) 1111111110

	// for hint
	direction int
	length    int
	sum       int
}

var (
	n     int
	board [20][20]block
	hintN int
	hints [400]int
	dxdy  [2][2]int = [2][2]int{
		{0, 1}, // horizontal (y,x)
		{1, 0}, // vertical (y,x)
	}
)

func inRange(y int, x int) bool {
	if (y > -1) && (y < n) && (x > -1) && (x < n) {
		return true
	}
	return false
}

func spread(y int, x int, num int) {
	// 가로,세로,위,아래
	var cy, cx int = y, x // currY, currX
	num = 1 << num
	board[cy][cx].bit = board[cy][cx].bit & (allBit - num)

	for d := horizontal; d <= vertical; d++ {
		// +
		for l := 1; ; l++ {
			cy = y + l*dxdy[d][0]
			cx = x + l*dxdy[d][1]
			if inRange(cy, cx) == false || board[cy][cx].color != white {
				break
			}
			board[cy][cx].bit = board[cy][cx].bit & (allBit - num)

		}

		// -
		for l := 1; ; l++ {
			cy = y - l*dxdy[d][0]
			cx = x - l*dxdy[d][1]
			if inRange(cy, cx) == false || board[cy][cx].color != white {
				break
			}
			board[cy][cx].bit = board[cy][cx].bit & (allBit - num)
		}

	}
}

func spreadCancel(y int, x int, num int) {
	var cy, cx int = y, x // currY, currX
	num = 1 << num
	board[cy][cx].bit = board[cy][cx].bit | num
	for d := horizontal; d <= vertical; d++ {
		// +
		for l := 1; ; l++ {
			cy = y + l*dxdy[d][0]
			cx = x + l*dxdy[d][1]
			if inRange(cy, cx) == false || board[cy][cx].color != white {
				break
			}
			board[cy][cx].bit = board[cy][cx].bit | num

		}

		// -
		for l := 1; ; l++ {
			cy = y - l*dxdy[d][0]
			cx = x - l*dxdy[d][1]
			if inRange(cy, cx) == false || board[cy][cx].color != white {
				break
			}
			board[cy][cx].bit = board[cy][cx].bit | num
		}

	}
}

func solution(hintIdx int, blockIdx int, subSum int) bool { //hint idx, block idx(sequence in hint)
	// 모든 경우를 지나 hintIdx가 끝에 도달했으면 성공.
	if hintIdx == hintN {
		return true
	}

	hintY, hintX := hints[hintIdx]/n, hints[hintIdx]%n
	hintDir := board[hintY][hintX].direction
	// hintSum = board[hintY][hintX].sum // 더 빠르게 하려하면 쓸듯
	hintLen := board[hintY][hintX].length
	y, x := hintY+blockIdx*dxdy[hintDir][0], hintX+blockIdx*dxdy[hintDir][1]

	// 다음 스텝의 값드을 미리 구해놓는다.
	var nextHintIdx, nextBlockIdx int
	if blockIdx < hintLen {
		nextHintIdx, nextBlockIdx = hintIdx, blockIdx+1
	} else {
		nextHintIdx, nextBlockIdx = hintIdx+1, 1
	}

	if blockIdx < hintLen {

		// 이미 값이 정해진 경우이면 지나간다.
		if board[y][x].value != notDefined {
			return solution(nextHintIdx, nextBlockIdx, subSum-board[y][x].value)
		}

		// 현재 위치(y,x)에서 가능한 값에서 다 시도해보고,
		tryCount := 0
		for num := 1; num <= 10; num++ {
			if (1<<num&board[y][x].bit) == 0 || subSum-num <= 0 {
				continue
			}
			// 시도하면서 자기를 주위 가로세로에서 제외함
			tryCount++
			board[y][x].value = num
			spread(y, x, num)
			// 퍼뜨리고 다음단계로 넘어간다.
			// 다음단계의 리턴값이 트루이면 트루를 리턴하고 끝낸다.

			if solution(nextHintIdx, nextBlockIdx, subSum-num) {
				return true
			}

			spreadCancel(y, x, num)
			board[y][x].value = notDefined
		}

	} else {
		if subSum <= 0 || subSum >= 10 {
			return false
		}

		var nextSubSum int
		if hintIdx+1 == hintN {
			nextSubSum = 0
		} else {
			nY, nX := hints[hintIdx+1]/n, hints[hintIdx+1]%n
			nextSubSum = board[nY][nX].sum
		}

		// 이미 숫자가 들어가잇는 경우 지나가면 됨
		if board[y][x].value != notDefined {
			return solution(nextHintIdx, nextBlockIdx, nextSubSum)
		}
		// 남은 값이 들어갈 수 있는지 확인하고 집어넣는다.
		subSumBit := 1 << subSum
		if board[y][x].bit&subSumBit == 0 {
			return false
		}

		spread(y, x, subSum)
		if solution(nextHintIdx, nextBlockIdx, nextSubSum) {
			return true
		}
		spreadCancel(y, x, subSum)
	}

	return false
}

func main() {
	stdin, err := os.OpenFile("input.txt", os.O_RDONLY|os.O_CREATE, 0666)
	if err != nil {
		fmt.Printf("input.txt does not exist")
		return
	}
	os.Stdin = stdin

	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d", &n)
		for y := 0; y < n; y++ {
			for x := 0; x < n; x++ {
				fmt.Scanf("%d", &board[y][x].color)
				if board[y][x].color == white {
					board[y][x].value = 0 // not_defined
					board[y][x].bit = 1111111110
				} else {
					board[y][x].value = 0
					board[y][x].bit = 0
				}

			}
		}
		fmt.Scanf("%d", &hintN)
		for hintCount := 0; hintCount < hintN; hintCount++ {
			var y, x, d, s, l int
			fmt.Scanf("%d %d %d %d", &y, &x, &d, &s)
			y-- // idx start from 0 (0 ~ n-1)
			x-- // idx start from 0 (0 ~ n-1)
			// get length
			for l = 1; ; l++ {
				var currY int = y + l*dxdy[d][0]
				var currX int = x + l*dxdy[d][1]
				if !inRange(currY, currX) || board[currY][currX].color != white {
					l--
					break
				}
			}
			board[y][x].color = hint
			board[y][x].direction = d
			board[y][x].length = l
			board[y][x].sum = s
			hints[hintCount] = y*n + x

		}
		/*
			for y := 0; y < n; y++ {
				for x := 0; x < n; x++ {
					fmt.Printf("%d ", board[y][x].color)
				}
				fmt.Println()
			}

			for i := 0; i < hintN; i++ {
				y := hints[i] / n
				x := hints[i] % n
				fmt.Println("(", y, x, ")", board[y][x].direction, board[y][x].length, board[y][x].sum)
			}
		*/
		firstHintY, firstHintX := hints[0]/n, hints[0]%n
		solution(0, 1, board[firstHintY][firstHintX].sum)
		for y := 0; y < n; y++ {
			fmt.Printf("%d", board[y][0].value)
			for x := 1; x < n; x++ {
				fmt.Printf(" %d", board[y][x].value)
			}
			fmt.Printf("\n")
		}
	}
}
