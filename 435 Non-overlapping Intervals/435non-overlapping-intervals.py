class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                end = min(intervals[i][1], end)
                res += 1
            elif intervals[i][0] >= end:
                end = intervals[i][1]
        return res


        