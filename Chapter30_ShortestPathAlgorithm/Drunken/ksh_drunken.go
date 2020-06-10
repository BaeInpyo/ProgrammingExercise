package main

import (
	"fmt"
	// "os"
)

const (
	inf = 87654321
)

var (
	nV    int
	nE    int
	costV [500]int
	costE [500][500]int

	crackdown [500][500]int
)

func main() {
	// os.Stdin, _ = os.OpenFile("input.txt", os.O_RDONLY, 0644)

	// input 받기
	fmt.Scanf("%d %d", &nV, &nE)
	for i := 0; i < nV; i++ {
		fmt.Scanf("%d", &costV[i])
	}

	for a := 0; a < nV; a++ {
		for b := 0; b < nV; b++ {
			costE[a][b] = inf
		}
		costE[a][a] = 0
	}
	var a, b, c int
	for i := 0; i < nE; i++ {
		fmt.Scanf("%d %d %d", &a, &b, &c)
		a, b = a-1, b-1
		costE[a][b] = c
		costE[b][a] = c
	}

	// shortest path 계산
	floyd()

	// 테스트 케이스 정답 출력
	var testcase int
	fmt.Scanf("%d", &testcase)
	for t := 1; t <= testcase; t++ {
		fmt.Scanf("%d %d", &a, &b)
		a, b = a-1, b-1
		fmt.Println(costE[a][b] + crackdown[a][b])
	}
}

func floyd() {
	for k := 0; k < nV; k++ {
		for a := 0; a < nV; a++ {
			for b := 0; b < nV; b++ {
				if k == a || k == b {
					continue
				}
				// 거리랑 단속 최악시간 까지 비교해야 되네
				old := costE[a][b] + crackdown[a][b]
				newCrackdown := max(crackdown[a][k], crackdown[k][b])
				newCrackdown = max(newCrackdown, costV[k])
				new := costE[a][k] + costE[k][b] + newCrackdown
				if old > new {
					costE[a][b] = new - newCrackdown
					costE[b][a] = new - newCrackdown
					crackdown[a][b] = newCrackdown
					crackdown[b][a] = newCrackdown
				}
			}
		}
	}
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

// http://blog.naver.com/PostView.nhn?blogId=namhong2001&logNo=221505860694&parentCategoryNo=&categoryNo=30&viewDate=&isShowPopularPosts=true&from=search
// 이렇게 하면 틀리는구나!
