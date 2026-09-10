class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = nums[0]
        res = nums[0]
        n = len(nums)

        for i in range(1,n):
            if running_sum < 0 and nums[i] > running_sum:
                running_sum = nums[i]
            else:
                running_sum += nums[i]
            
            res = max(res, running_sum)
        
        return res