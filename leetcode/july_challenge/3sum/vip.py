class Solution:
    def next_idx(self, i, nums):
        while i < len(nums) - 1:
            i += 1;
            if nums[i-1] != nums[i]:
                break
        return i;
    
    def prev_idx(self, i, nums):
        while i > 0:
            i -= 1;
            if nums[i] != nums[i+1]:
                break;
        return i;
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [];
        nums.sort();
        nums_len = len(nums);
        if (nums_len < 3):
            return ans;
        
        a_idx = 0;
        while a_idx < (nums_len - 2):
            if a_idx > 0 and nums[a_idx-1] == nums[a_idx]:
                a_idx += 1;
                continue;
            b_idx = a_idx + 1;
            c_idx = nums_len - 1;

            while b_idx < c_idx:
                ab_sum = nums[a_idx] + nums[b_idx];
                if ab_sum > 0:
                    break;
                   
                t_sum = ab_sum + nums[c_idx];

                if t_sum < 0:
                    b_idx = self.next_idx(b_idx, nums);
                elif t_sum == 0:
                    ans.append([nums[a_idx], nums[b_idx], nums[c_idx]]);
                    b_idx = self.next_idx(b_idx, nums);
                    c_idx = self.prev_idx(c_idx, nums);
                else:
                    c_idx = self.prev_idx(c_idx, nums);

            a_idx = self.next_idx(a_idx, nums);

        return ans;
