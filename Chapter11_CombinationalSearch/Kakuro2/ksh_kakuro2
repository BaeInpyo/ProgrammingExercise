// hints 전부다 재귀 돌면서
// 차근차근 만족시켜 나가면되지 않을까..
// 그리고 하나를 채워넣으면 이거에 의해 변하는 애들을
// can[][]에 기록하고..

package main

import (
	"fmt"
	"os"
)

type location struct {
	y int
	x int
}

type feature struct {
	direction int
	sum       int
	length    int
}

const (
	maxN int = 20

	horizontal int = 0
	vertical   int = 1

	blackBlk int = 0
	whiteBlk int = 1
	hintBlk  int = 2
)

var (
	kinds       [20][20]int // 0: blackBlk, 1: whiteBlk, -1: hintBlk
	hintN       int
	hints       map[*location]*feature
	orderHint   [400]*location
	board       [20][20]int // 0: black,hint, number : white
	can         [20][20]int // 1 1 1 1 1 1 1 1 1 0
	boardLength int

	dxdy = []location{
		location{
			y: 0,
			x: 1,
		},
		location{
			y: 1,
			x: 0,
		},
	}
)

func reset() {
	for y := 0; y < boardLength; y++ {
		for x := 0; x < boardLength; x++ {
			kinds[y][x] = 0
			board[y][x] = 0
		}
	}
	hints = make(map[*location]*feature)
}

func inRange(y int, x int) bool {
	if y > -1 || y < boardLength || x > -1 || x < boardLength {
		return true
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
		fmt.Scanf("%d", &boardLength)
		reset()
		for y := 0; y < boardLength; y++ {
			for x := 0; x < boardLength; x++ {
				fmt.Scanf("%d", &kinds[y][x])
			}
		}
		fmt.Scanf("%d", &hintN)
		for hintCount := 0; hintCount < hintN; hintCount++ {
			var y, x, d, s, l int
			fmt.Scanf("%d %d %d %d", &y, &x, &d, &s)
			y-- // idx start from 0
			x-- // idx start from 0
			// get length
			for l = 1; ; l++ {
				var currY int = y + l*dxdy[d].y
				var currX int = x + l*dxdy[d].x
				if !inRange(currY, currX) || kinds[currY][currX] != whiteBlk {
					l--
					break
				}
			}
			var loc location = location{y, x}
			var feat feature = feature{d, s, l}
			kinds[y][x] = hintBlk
			orderHint[hintCount] = &loc
			hints[&loc] = &feat
		}
		/*
			for y := 0; y < boardLength; y++ {
				for x := 0; x < boardLength; x++ {
					fmt.Printf("%d ", kinds[y][x])
				}
				fmt.Println()
			}

			for i := 0; i < hintN; i++ {
				var loc *location = orderHint[i]
				fmt.Println(*loc, " : ", *(hints[loc]))
			}
		*/
	}
}
