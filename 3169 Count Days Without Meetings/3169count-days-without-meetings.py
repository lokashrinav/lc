class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[0], x[1]))  

        curr = []
        curr.append(meetings[0])
        for i in range(1, len(meetings)):
            if meetings[i][0] <= curr[-1][1]:
                meet = curr.pop()
                curr.append([min(meetings[i][0], meet[0]), max(meetings[i][1], meet[1])])
            else:
                curr.append(meetings[i])
        
        curr.insert(0, [0, 0])
        curr.append([days + 1, days + 1])
        total = 0
        print(curr)
        for i in range(1, len(curr)):
            total += curr[i][0] - curr[i - 1][1] - 1

        return total


