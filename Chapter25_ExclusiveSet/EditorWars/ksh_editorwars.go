package main

import (
	"fmt"
	"os"
)

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
	for a != belongsTo[a] {
		a = belongsTo[a]
	}
	return a
}
func union(a int, b int) int {
	if a == -1 || b == -1 {
		if a < b {
			return a
		}
		return b
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

func ack(a int, b int) (int, bool) {
	// a가 싫어하는 집단이 b집단인지 봐야함 -> 실패
	// b가 싫어하는 집단이 a집단인지 봐야함 -> 실패
	// a,b를 union해준다.
	// 그리고 리턴받은 값(합쳐진 부모)의 dislike를 바꿔준다.
	// a,b가 서로 싫어하는 집단이 같은 집단으로 합칠수있는지 또 check_union해야함
	pa := find(a)
	pb := find(b)

	if dislike[pa] == pb {
		return -1, false
	} // 적대관계이다. 어차피 쌍방이므로 한쪽만 보면될듯...

	pp := union(pa, pb)
	dd, ok := ack(pa, pb)
	if ok == false {
		return -1, false
	}
	dislike[pp] = dd
	if dd != -1 {
		dislike[dd] = pp
	}
	return pp, false
}

func dis(a int, b int) bool {
	// a가 싫어하는 집단이 b집단인지 봐야함 -> 실패
	// b가 싫어하는 집단이 a집단인지 봐야함 -> 실패
	// a,b를 union해준다.
	// 그리고 리턴받은 값(합쳐진 부모)의 dislike를 바꿔준다.
	// a,b가 서로 싫어하는 집단이 같은 집단으로 합칠수있는지 또 check_union해야함
	pa := find(a)
	pb := find(b)
	if pa == pb {
		return false
	}
	// pa의 적이랑 pb랑 짝이고
	// pb의 적이랑 pa랑 짝이다.
	na, ok := ack(pa, dislike[pb])
	if ok == false {
		return false
	}
	nb, ok := ack(pb, dislike[pa])
	if ok == false {
		return false
	}
	dislike[na] = nb
	dislike[nb] = na
	return true
}
func solution() int {
	var idx int
	for idx = 1; idx <= m; idx++ {
		var ok bool
		if input[idx].command == ackType {
			_, ok = ack(input[idx].a, input[idx].b)
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

	return -1
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
		var idx int
		for idx = 1; idx <= m; idx++ {
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

/*
내가 a <-> b를 만들고
그리고 c-a를 만들었는데..
b랑 c가 ACK가 왔다.
이때 에러를 실패를 리턴해야하는데?
union할때 dislike도 같이 옮겨줘야할듯

그때 만약에 dislike가 둘다 있으면 또 같이 두개를 같이 union해줘야하고.

그렇게 같이 만들어주면... 뭘해야하지?
1번부터 돌면서 짝이없는애들은 서로 배척하는집단중에서는...큰놈을
상관없는 애들은 그냥 싹다 모아서
이렇게해야하는데.. 서로 배척하는 집단을 가져왔을때 패런트가 더 큰경우에만 계산
*/

/*
MAX PARTY SIZE IS 3
MAX PARTY SIZE IS 100
CONTRADICTION AT 3
MAX PARTY SIZE IS 5
*/
