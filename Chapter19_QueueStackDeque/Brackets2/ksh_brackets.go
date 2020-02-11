package main

import "fmt"

var stack [10000]byte

func main() {
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		var input string
		fmt.Scanln(&input)
		top, lenStr := -1, len(input)
		for i := 0; i < lenStr; i++ {
			if input[i] == '(' || input[i] == '{' || input[i] == '[' {
				top++
				stack[top] = input[i]
			} else {
				if top == -1 {
					top = -2
					break
				}
				if input[i] == stack[top]+1 || input[i] == stack[top]+2 {
					top--
				} else {
					break
				}
			}
		}
		if top == -1 {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
	}
	return
}
