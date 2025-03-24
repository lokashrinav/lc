class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        curr = skill[::]
        for i in range(1, len(curr)):
            curr[i] += curr[i - 1]

        prev = 0
        idk = sum(skill)

        for i in range(len(mana)):
            total = prev + mana[i] * idk
            if i < len(mana) - 1:
                minPrev = prev + mana[i] * curr[0]
                for p in range(1, len(curr)):
                    minPrev = max(minPrev, prev + mana[i] * curr[p] - mana[i + 1] * curr[p - 1])
                prev = minPrev
            else:
                return total