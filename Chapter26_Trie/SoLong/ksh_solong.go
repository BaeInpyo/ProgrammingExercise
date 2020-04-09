package main

import (
	"fmt"
	//"os"
)

const (
	ALPHABETS = 26
	EMPTY     = ""
)

var (
	N     int
	M     int
	freq  map[string]int
	index map[string]int
)

func toNumber(ch byte) int {
	return int(ch - 'A')
}

type TrieNode struct {
	children  [ALPHABETS]*TrieNode
	recommend string
	terminal  bool
}

func (node *TrieNode) insert(curr int, key *string) {
	// update recommend
	var reco *string = &(node.recommend)
	if freq[*reco] < freq[*key] {
		node.recommend = *key
	} else if (freq[*reco] == freq[*key]) && (*reco > *key) {
		node.recommend = *key
	}

	if curr == len(*key) {
		node.terminal = true
	} else {
		next := toNumber((*key)[curr])
		if node.children[next] == nil {
			node.children[next] = new(TrieNode)
			node.children[next].terminal = false
			node.children[next].recommend = *key
		}
		node.children[next].insert(curr+1, key)
	}
}

func (node *TrieNode) find(curr int, key *string) int {
	// 레코멘드가 자기자신인 경우 끝
	var reco *string = &(node.recommend)
	if index[*reco] == index[*key] {
		return curr
	}
	next := toNumber((*key)[curr])
	return node.children[next].find(curr+1, key)
}

func main() {
	//os.Stdin, _ = os.OpenFile("input.txt", os.O_RDONLY, 0666)
	var testcase int
	fmt.Scanf("%d", &testcase)
	for tc := 1; tc <= testcase; tc++ {
		fmt.Scanf("%d %d", &N, &M)
		var s string
		var f int
		freq = make(map[string]int)
		index = make(map[string]int)
		for i := 0; i < N; i++ {
			fmt.Scanf("%s %d", &s, &f)
			freq[s] = f
			index[s] = i
		}

		var head TrieNode
		makeTrie(&head)
		head.recommend = EMPTY
		head.terminal = false

		fmt.Printf("%d\n", calc(&head))
	}

}

func makeTrie(head *TrieNode) {
	for key := range freq {
		head.insert(0, &key)
	}
}

func calc(head *TrieNode) int {
	var result int = 0
	var str string
	for i := 0; i < M; i++ {
		fmt.Scanf("%s", &str)
		if _, ok := index[str]; !ok {
			result += len(str)
		} else {
			result += head.find(0, &str) + 1
		}
	}

	return result + M - 1
}
