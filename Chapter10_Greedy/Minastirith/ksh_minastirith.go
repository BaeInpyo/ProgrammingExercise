// 이거 그.. 한바퀴를 아예 돌아야 하네.. 그니까 0도인애들도 다시 한번 봐야하네 (시작점인 나를 빼고)
// 위에 내용 추가해보자
package main

import (
	"fmt"
	"math"
	//"os"
	//"sort"
)

const (
	pi         float64 = math.Pi
	impossible int     = 987654321
	error      float64 = 0.00000001
)

var n int

type pair struct {
	alpha float64
	beta  float64
}

var covers [100]pair

func contain(cover *pair, angle float64) bool {
	if (cover.alpha-error <= angle) && (angle <= cover.beta+error) {
		return true
	}
	return false
}
func check(pivot *pair, start int) int {
	count := 1
	// 지금 경계를 포함하고 있는 애들 중에서 계속해서 늘리다가
	// 이 경계를 포함할수 없는 애가 나타나면
	// 제일 멀리갔던애를 이제 경계로 바꾸고
	// 똑같은 과정 반복
	totalAlpha := pivot.alpha
	totalBeta := pivot.beta
	oneRound := totalAlpha + 2*pi
	idx := start
	end := n + start
	for idx < end {
		// 이미 다 돌았으면 끝
		if oneRound <= totalBeta+error {
			break
		}
		// 지금 beta를 포함하는 애 전부다 while loop 돌아서 최대값 가져오기
		maxBeta := totalBeta
		canConnect := false
		for idx < end && contain(&covers[idx], totalBeta) {
			if maxBeta <= covers[idx].beta {
				canConnect = true
				maxBeta = covers[idx].beta
			}
			idx++
		}
		if canConnect {
			count++
			totalBeta = maxBeta
			idx--
		}
		idx++
	}
	if oneRound <= totalBeta+error {
		return count
	}
	return impossible
}
func solution() {
	// for-loop : members contain 0 radian
	var contain0IdxBound int = n
	for i := 0; i < n; i++ {
		if contain(&covers[i], 0) == false {
			contain0IdxBound = i
			break
		}
	}
	// 뒤에다가 0인애들 추가(한바퀴 돌고 아예 돌아가기 위해서)
	for i := 0; i < contain0IdxBound; i++ {
		covers[n+i].alpha = covers[i].alpha
		covers[n+i].beta = covers[i].beta
	}
	minCount := impossible

	for i := 0; i < contain0IdxBound; i++ {
		pivot := &covers[i]
		start := contain0IdxBound
		count := check(pivot, start)
		if count < minCount {
			minCount = count
		}
	}
	if minCount == impossible {
		fmt.Println("IMPOSSIBLE")
	} else {
		fmt.Println(minCount)
	}

}
func posToRadian(y, x, r float64) (float64, float64) {
	centor := math.Atan2(y, x) // (-pi..pi]
	if centor < 0 {
		centor += 2 * pi // [0.. 2*pi)
	}
	theta := math.Asin(r / 16)
	alpha := centor - 2*theta
	beta := centor + 2*theta
	return alpha, beta
}

func main() {
	// stdin=input.txt
	// stdin, err := os.OpenFile("input.txt", os.O_RDONLY|os.O_CREATE, 0666)
	// if err != nil {
	// 	fmt.Printf("input.txt does not exist")
	// 	return
	// }
	// os.Stdin = stdin

	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d", &n)
		for i := 0; i < n; i++ {
			var y, x, r float64
			fmt.Scanf("%f %f %f", &y, &x, &r)
			covers[i].alpha, covers[i].beta = posToRadian(y, x, r)
			if contain(&covers[i], 2*pi) {
				covers[i].alpha -= 2 * pi
				covers[i].beta -= 2 * pi
			}
		}

		for pivot := 0; pivot < n; pivot++ {
			for i := pivot - 1; i >= 0; i-- {
				if covers[i].alpha < covers[i+1].alpha {
					break
				}
				tempAlpha := covers[i].alpha
				tempBeta := covers[i].beta
				covers[i].alpha = covers[i+1].alpha
				covers[i].beta = covers[i+1].beta
				covers[i+1].alpha = tempAlpha
				covers[i+1].beta = tempBeta
			}
		}

		solution()
	}
}
