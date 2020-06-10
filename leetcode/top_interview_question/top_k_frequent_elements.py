"""
Problem URL: https://leetcode.com/problems/top-k-frequent-elements/

1. In case of "TOP K" problems, build heap can be a solution because time
complexity of building heap is O(n) which is faster than sorting and pick K
elements whose time complexity is O(nlogn).

2. We can manually iterate from n to 0 in terms of coun .
"""



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # with heap
        # import heapq
        # count_dict = dict()
        # for num in nums:
        #     if num in count_dict:
        #         count_dict[num] += 1
        #     else:
        #         count_dict[num] = 1

        # heap = [(-count, num) for (num, count) in count_dict.items()]
        # heapq.heapify(heap) # build heap within O(n)
        # result = []
        # for _ in range(k):
        #     result.append(heapq.heappop(heap)[1])

        # return result

        # # with manual count
        count_dict = dict() # key: num, value: number of appearance
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        reverse_count_dict = dict()  # key: count, value: num that appears `count` times
        for (num, count) in count_dict.items():
            if count in reverse_count_dict:
                reverse_count_dict[count].append(num)
            else:
                reverse_count_dict[count] = [num]

        result = []
        for count in reversed(range(1, len(nums)+1)):
            if count in reverse_count_dict:
                result.extend(reverse_count_dict[count])

        return result[:k]