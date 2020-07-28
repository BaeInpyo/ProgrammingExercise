class Solution:
    def partition(self, nums, start, end):
        if start == end or start + 1 == end:
            return min(nums[start], nums[end])
        
        mid = (start + end) // 2
        
        if nums[mid] > nums[end]:
            return self.partition(nums, mid, end)
        elif nums[mid] == nums[end]:
            return min(self.partition(nums, mid, end), self.partition(nums, start, mid))
        return self.partition(nums, start, mid)
    
    def findMin(self, nums: List[int]) -> int:
        return self.partition(nums, 0, len(nums)-1)
