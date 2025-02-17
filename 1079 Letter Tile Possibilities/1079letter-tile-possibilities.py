class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        # 3! / 1! 2! = 3

        # 2 / 2

        hmap = Counter(tiles)

        def dfs(curr):
            count = 0

            for key in hmap.keys():
                if hmap[key]:
                    hmap[key] -= 1
                    count += 1
                    curr.append(key)
                    count += dfs(curr)
                    curr.pop()
                    hmap[key] += 1

            return count

        return dfs([])

