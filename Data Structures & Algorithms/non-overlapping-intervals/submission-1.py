class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_start,prev_end = intervals[0] 
        removals = 0
        # print(intervals)

        # # 47            54          65         
        # # [-73, -26], [-65, -11], [-63, 2], [-62, -49], [-52, 31], [-40, -26], [-31, 49], 

        for i in range(1,len(intervals)):
            if intervals[i][0] >= prev_end:
                prev_start, prev_end = intervals[i]
            else:
                if intervals[i][1] <= prev_end:
                    prev_start, prev_end = intervals[i]

                removals += 1
        return removals


            


