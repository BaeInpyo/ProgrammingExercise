class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for idx, num in enumerate(nums):
            if numDict.get(target-num, -1) != -1:
                return [numDict[target-num], idx]
            numDict[num] = idx
