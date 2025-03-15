class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr, left, right):
            if len(curr) == n * 2:
                if left == right:
                    res.append(''.join(curr))
                return
            
            if left < n:
                curr.append("(")
                dfs(curr, left + 1, right)
                curr.pop()

            if right < left:
                curr.append(")")
                dfs(curr, left, right + 1)
                curr.pop()

        dfs([], 0, 0)

        return res