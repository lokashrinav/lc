class Solution:
    def crackSafe(self, n: int, k: int) -> str:

        def dfs(curr, seen, total):
            if curr[-n:] in seen: return
            seen.add(curr[-n:])
            if len(seen) == total: return curr

            for c in range(k):
                final = dfs(curr + str(c), seen, total)
                if final:
                    return final
            seen.remove(curr[-n:])

        return dfs("0" * n, set(), k ** n)



        