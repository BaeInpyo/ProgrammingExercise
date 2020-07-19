import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        freq_dict = {}
        for n in nums:
            if n not in freq_dict:
                freq_dict[n] = 1
            else:
                freq_dict[n] += 1
        
        for key in freq_dict:
            if len(heap) < k:
                heappush(heap, (freq_dict[key], key))
            else:
                if freq_dict[key] > heap[0][0]:
                    heappushpop(heap, (freq_dict[key], key))
        
        return [elem[1] for elem in heap]
