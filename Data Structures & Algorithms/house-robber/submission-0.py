class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1: 
            return max(nums)

        previous, neighbor = nums[0], nums[1]
        
        for i in range(2, n):
            nums[i] += previous
            previous = max(neighbor, previous)
            neighbor = nums[i]
            
        return max(nums[n-1], nums[n-2])

            