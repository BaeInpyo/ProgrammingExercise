package main

import (
	"fmt"
	"os"
)

var (
	belongsTo [10000]int
	dislike   [10000]int
	height    [10000]int
	weight    [10000]int
	n, m      int
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
	for a != belongsTo[a] {
		a = belongsTo[a]
	}
	return a
}
func union(a int, b int) int {
	pa := find(a)
	pb := find(b)
	if pa == pb {
		return pa
	}
	if height[pa] < height[pb] {
		belongsTo[pa] = pb
		weight[pb] += weight[pa]
		return pb
	} else if height[pa] > height[pb] {
		belongsTo[pb] = pa
		weight[pa] += weight[pb]
		return pa
	} else {
		belongsTo[pb] = pa
		weight[pa] += weight[pb]
		height[pa]++
		return pa
	}
}

func checkUnion(a int, b int) bool {
	// a가 싫어하는 집단이 b집단인지 봐야함 -> 실패
	// b가 싫어하는 집단이 a집단인지 봐야함 -> 실패
	// a,b를 union해준다.
	// 그리고 리턴받은 값(합쳐진 부모)의 dislike를 바꿔준다.
	// a,b가 서로 싫어하는 집단이 같은 집단으로 합칠수있는지 또 check_union해야함

}

func main() {
	stdin, _ := os.OpenFile("input.txt", os.O_RDONLY, 0666)
	os.Stdin = stdin
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d %d", &n, &m)
		initialize()
		var comment string
		var a, b int
		var idx int
		for idx = 1; idx <= m; idx++ {
			fmt.Scanf("%s %d %d", &comment, &a, &b)
			if comment == "ACK" {
				// a,b랑 합쳐주면 되는데
				checkUnion(a, b)
			} else {
				// a, b가 적대관계이면.. 서로 부모의 dislike에 넣어주고..
				// 만약에 같은 부모이면 충돌..
				// 이미 pa집단에 싫어하는 모임이 있다면 check_union
				// 이미 pb집단에 싫어하는 모임이 있다면 check_union
				pa := find(a)
				pb := find(b)
				if pa == pb {
					break
				}
				if dislike[pa] == -1 {
					dislike[pa] = pb
				} else {
					if !checkUnion(dislike[pa], pb) {
						break
					}
				}
				if dislike[pb] == -1 {
					dislike[pb] = pa
				} else {
					if !checkUnion(dislike[pb], pa) {
						break
					}
				}
			}
		}
		// if idx <= m {
		// 	fmt.Printf("CONTRADICTION AT %d\n", idx)
		// } else {
		// 	fmt.Printf("MAX PARTY SIZE IS %d\n", calcMax())
		// }

	}
}

/*
내가 a <-> b를 만들고
그리고 c-a를 만들었는데..
b랑 c가 ACK가 왔다.
이때 에러를 실패를 리턴해야하는데?
union할때 dislike도 같이 옮겨줘야할듯

그때 만약에 dislike가 둘다 있으면 또 같이 두개를 같이 union해줘야하고.

그렇게 같이 만들어주면... 뭘해야하지?
1번부터 돌면서 짝이없는애들은 서로 배척하는집단중에서는...큰놈을
이렇게하면 두번계산하게되는데.. 어떻게 한번만 계산하지
*/
/*
MAX PARTY SIZE IS 3
MAX PARTY SIZE IS 100
CONTRADICTION AT 3
MAX PARTY SIZE IS 5
*/
