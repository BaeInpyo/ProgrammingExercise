class Solution:
    def subsets_internal(self, nums: List[int], start: int) -> List[List[int]]:
        if len(nums)-1 == start:
            return [[], [nums[start]]]
        
        result = self.subsets_internal(nums, start+1)
        cnt = len(result)
        for i in range(0, cnt):
            result.append(result[i] + [nums[start]])
            
        return result
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsets_internal(nums, 0)
