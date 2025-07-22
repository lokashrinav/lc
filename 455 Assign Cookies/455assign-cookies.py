class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        players, trainers = g, s
        ans = 0

        players.sort()
        trainers.sort()

        for i, trainer in enumerate(trainers):
            if players[ans] <= trainer:
                ans += 1
                if ans == len(players):
                    return ans

        return ans  