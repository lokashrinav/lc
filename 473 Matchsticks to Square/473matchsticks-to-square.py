class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        size = sum(matchsticks)

        if size % 4 != 0:
            return False
        
        size //= 4
        hmap = Counter(matchsticks)
        memo = {}

        def dfs(curr, count):
            if count == 4:
                return True
            if curr == 0:
                return dfs(size, count + 1)
            if curr < 0:
                return False
            if tuple(hmap.items()) in memo:
                return memo[tuple(hmap.items())]

            for key in hmap.keys():
                if hmap[key]:
                    hmap[key] -= 1
                    if dfs(curr - key, count):
                        return True
                    hmap[key] += 1
            
            memo[tuple(hmap.items())] = False

            return False

        return dfs(size, 0)

        