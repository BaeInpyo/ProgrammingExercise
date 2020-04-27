package main

import (
	"fmt"
	// "os"
	"strconv"
)

var (
	n     int
	step  map[string]int
	input [8]int

	queue [50000]string
	front int
	rear  int
)

func qPush(str string) {
	rear++
	queue[rear] = str
}
func qPop() string {
	result := queue[front]
	front++
	return result
}

func qIsEmpty() bool {
	if rear < front {
		return true
	}
	return false
}

func reverse(str *string, start int, end int) string { // start, end are closed interval
	bytes := []byte(*str)
	for i, j := start, end; i < j; i, j = i+1, j-1 {
		bytes[i], bytes[j] = bytes[j], bytes[i]
	}
	return string(bytes)
}
func main() {
	// os.Stdin, _ = os.OpenFile("input.txt", os.O_RDONLY, 0644)

	step = make(map[string]int)
	var sortedString string = ""
	for i := 1; i <= 8; i++ {
		sortedString += strconv.Itoa(i)
		front = 0
		rear = -1
		preCalc(sortedString)
	}

	var testcase int
	fmt.Scanf("%d", &testcase)

	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d", &n)
		for i := 0; i < n; i++ {
			fmt.Scanf("%d", &input[i])
		}
		var generalString string = generalize()

		fmt.Println(step[generalString])
	}
}
func generalize() string {
	result := ""
	for a := 0; a < n; a++ {
		smaller := 1
		for b := 0; b < n; b++ {
			if input[b] < input[a] {
				smaller++
			}
		}
		result += strconv.Itoa(smaller)
	}

	return result
}

func preCalc(sorted string) {
	step[sorted] = 0
	qPush(sorted)

	n := len(sorted)
	for !qIsEmpty() {
		curr := qPop()
		prevStep := step[curr]
		// curr 에서 전체 스왑하는 경우 다 해보는데,, 이미 step에 기록된 애면 넘어간다.
		for i := 0; i < n; i++ {
			for j := i + 1; j < n; j++ {
				next := reverse(&curr, i, j)
				if _, ok := step[next]; !ok {
					step[next] = prevStep + 1
					qPush(next)
				}
			}
		}
	}
}
