class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals.sort()
        res = [intervals[0]]
        

        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1] = [
                    min(res[-1][0], intervals[i][0]),
                    max(res[-1][1], intervals[i][1])
                ]
        
        return res