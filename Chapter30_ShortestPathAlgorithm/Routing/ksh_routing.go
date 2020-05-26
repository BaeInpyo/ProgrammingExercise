// 음.. 어차피 인접한 점들을 리스트로 안가지고 어레이로 가지고있으면
// 결국은 쭉 다 돌아봐야하니까 (최단거리를 업데이트 하기위해)
// 이때 그냥 쭉 돌면서 최소 값을 기억하는게
// priority queue도 안써도 되고, 더 좋은 것 같은데?
// 아하.. sparse하면 pq가 훨씬 좋구나.
// 지금 문제는 vertex는 10,000개인데, nedge가 20,000개이니까..
// 어레이로 담으면 메모리 사이즈도 터지겠네
package main

import (
	"container/heap"
	"fmt"
	// "os"
)

//////////////////////////////////////////////////////////////////
// priority queue
type Item struct {
	value    int     // The value of the item; arbitrary.
	priority float64 // The priority of the item in the queue.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].priority > pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

// update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) update(item *Item, value int, priority float64) {
	item.value = value
	item.priority = priority
	heap.Fix(pq, item.index)
}

//////////////////////////////////////////////////////////////////
const (
	inf = 1 << 500
)

var (
	nvertex int
	nedge   int

	adjacency [10000][]int
	noise     [10000][]float64

	dist [10000]float64
)

func initialize() {
	for i := 0; i < nvertex; i++ {
		adjacency[i] = make([]int, 0, 8) //20000 * 8 * 10 = 1,600,000
		noise[i] = make([]float64, 0, 8)
		dist[i] = float64(inf)
	}

}

func main() {
	// os.Stdin, _ = os.OpenFile("input.txt", os.O_RDONLY, 0644)
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d %d", &nvertex, &nedge)
		initialize()
		for i := 0; i < nedge; i++ {
			var left, right int
			var weight float64
			fmt.Scanf("%d %d %f", &left, &right, &weight)
			// for left
			adjacency[left] = append(adjacency[left], right)
			noise[left] = append(noise[left], weight)
			// for right
			adjacency[right] = append(adjacency[right], left)
			noise[right] = append(noise[right], weight)

		}
		fmt.Printf("%0.10f\n", solution())
	}
}

func solution() float64 {
	// pq에 0에서 갈수있는 애들 다 넣어두고,,
	// 시작하면 됨
	dist[0] = 1
	pq := make(PriorityQueue, 0)
	heap.Init(&pq)
	item := &Item{
		value:    0,
		priority: 1,
	}

	heap.Push(&pq, item)

	for pq.Len() != 0 {
		item := heap.Pop(&pq).(*Item)
		here := item.value
		cost := item.priority
		// 지금꺼낸것보다 이미 더 짧은 경로를 알고있으면 얘는 필요없는 애
		if dist[here] < cost {
			continue
		}
		// 인접한 정점 모두 검사
		for i, _ := range adjacency[here] {
			there := adjacency[here][i]
			thereCost := cost * noise[here][i]
			// 더 짧은 값으로 갱신하게 되는 경우 pq에 넣는다.
			if dist[there] > thereCost {
				dist[there] = thereCost
				item := &Item{
					value:    there,
					priority: thereCost,
				}
				heap.Push(&pq, item)
			}
		}
	}
	return dist[nvertex-1]
}
