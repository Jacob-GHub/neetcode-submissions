class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        for i in range(n):
            if i <= 1:
                continue
            cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[n-1],cost[n-2])