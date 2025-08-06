class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hmap = defaultdict(int)

        for i in range(len(wall)):
            curr = 0
            for p in range(len(wall[i]) - 1):
                curr += wall[i][p]
                hmap[curr] += 1

        maxNum = 0
        saved = None

        for key, val in hmap.items():
            if val > maxNum:
                maxNum = val
                saved = key

        return len(wall) - maxNum
