class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = collections.defaultdict(int)
        n = len(nums)

        def makeLIS(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            
            sequence = 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    sequence = max(sequence, 1 + makeLIS(j))
            dp[i] = sequence
            return sequence

        for i in range(n):
            if i not in dp:
                makeLIS(i)
        return max(dp.values())