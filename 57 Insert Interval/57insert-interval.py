class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            if newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                return intervals
            elif newInterval[0] > intervals[i][1]:
                i += 1
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                intervals.pop(i)

        intervals.append(newInterval) # 1, 5
        return intervals

            

