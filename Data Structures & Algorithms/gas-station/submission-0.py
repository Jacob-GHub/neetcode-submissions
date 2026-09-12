class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        accumulated = 0
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1

        start_index = 0
        for i in range(n):
            if accumulated < 0:
                start_index = i
                accumulated = 0
            accumulated += gas[i]
            accumulated -= cost[i]
        return start_index

