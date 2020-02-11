package main

import "fmt"

var maxInt uint64 = (1 << 32)
var queue [5000001]uint64
var mod int = 5000001
var front int
var rear int

func queueIsNotEmpty() bool {
	//  (0, -1), (n, n-1) (0, 5000000)
	var rear2 int = rear - mod
	if rear == front-1 || rear2 == front-1 {
		return false
	}
	return true
}
func queuePush(num uint64) {
	rear = (rear + 1) % mod
	queue[rear] = num
}
func queuePop() uint64 {
	var result uint64 = queue[front]
	front = (front + 1) % mod
	return result
}
func initialize() {
	front = 0 // 빼고 더한다
	rear = -1 // 더하고 넣는다.
}
func main() {
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		var n int
		var k uint64
		initialize()
		fmt.Scanf("%d %d", &k, &n)
		var input uint64 = 1983
		var sum uint64 = 0
		var count int = 0
		for i := 1; i <= n; i++ {
			signal := (input % 10000) + 1
			queuePush(signal)
			input = (input*214013 + 2531011) % maxInt
			sum += signal
			for queueIsNotEmpty() {
				if sum == k {
					count++
					break
				} else if sum < k {
					break
				} else {
					prev := queuePop()
					sum -= prev
				}
			}
		}
		fmt.Println(count)
	}
}
