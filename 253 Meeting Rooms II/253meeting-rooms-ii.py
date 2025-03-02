class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        
        start = [intervals[i][0] for i in range(len(intervals))]
        end = [intervals[i][1] for i in range(len(intervals))]

        start.sort()
        end.sort()

        ind1, ind2 = 0, 0
        curr = 0
        maxNum = 0
        while ind1 < len(start) and ind2 < len(end):
            if start[ind1] < end[ind2]:
                ind1 += 1
                curr += 1
            elif end[ind2] > start[ind1]:
                ind2 += 1
                curr -= 1
            else:
                ind2 += 1
                ind1 += 1
            maxNum = max(curr, maxNum)
        
        return maxNum
