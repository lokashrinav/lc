"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule):
        # Step 1: Collect all intervals
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])
        
        # Step 2: Sort and merge
        intervals.sort()
        merged = []
        
        for start, end in intervals:
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        # Step 3: Find gaps
        result = []
        for i in range(len(merged) - 1):
            gap_start = merged[i][1]
            gap_end = merged[i + 1][0]
            if gap_start < gap_end:
                result.append(Interval(gap_start, gap_end))
        
        return result