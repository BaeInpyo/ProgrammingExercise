"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3384/
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []

        # by sorting, we can easily skip duplicates
        nums = sorted(nums)

        for idx in range(len(nums)):
            # since nums are sorted, there cannot be 3sums
            if nums[idx] > 0:
                break

            # skip duplicate target
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            target = nums[idx]

            # we use 2 pointers
            # if we move left to right, sum gets bigger
            # if we move right to left, sum gets smaller
            left, right = idx+1, len(nums)-1
            while left < right:
                # sum need to shrink
                if nums[left] + nums[right] > -target:
                    right -= 1

                # sum need to grow
                elif nums[left] + nums[right] < -target:
                    left += 1

                # found 3sum
                else:
                    answer.append([target, nums[left], nums[right]])
                    # skip duplicates
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    # skip duplicates
                    while left<right and nums[right-1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1

        return answer
