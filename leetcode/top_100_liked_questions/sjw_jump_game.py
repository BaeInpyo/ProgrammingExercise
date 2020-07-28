"""
Problem URL: https://leetcode.com/problems/jump-game/
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.sol2(nums)
        
            
    def sol1(self, nums):
        """Solve with list"""
        reachable = [False] * len(nums)
        reachable[0] = True
        for idx in range(len(nums)):
            if not reachable[idx]:
                break
                
            end = min(len(nums), idx + nums[idx])
            reachable[idx+1:end+1] = [True] * (end-idx)
            # print("idx, reachable:", idx, reachable)
            
        else:
            return True
        
        return False
    
    def sol2(self, nums):
        """List is too expensive, use int instead"""
        reachable = nums[0]
        for idx in range(len(nums)):
            if idx > reachable:
                break
                
            reachable = max(reachable, idx+nums[idx])
            # print("idx, reachalbe", idx, reachable)
            
        else:
            return True
        
        return False