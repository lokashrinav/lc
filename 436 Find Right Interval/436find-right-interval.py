class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        arr = [-1] * len(intervals)
        hmap = {}
        starting = []
        for i in range(len(intervals)):
            hmap[intervals[i][0]] = i
            starting.append(intervals[i][0])

        starting.sort()

        res = []
        for i in range(len(intervals)):
            l, r = 0, len(starting) - 1
            saved = float('inf')
            while l <= r:
                m = (l + r) // 2
                if intervals[i][1] <= starting[m]:
                    r = m - 1
                    saved = min(saved, m)
                else:
                    l = m + 1

            res.append(hmap[starting[saved]] if saved != float('inf') else -1)

        return res


