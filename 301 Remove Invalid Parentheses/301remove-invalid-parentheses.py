class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def valid(s):
            balance = 0
            for i in range(len(s)):
                if s[i] == "(":
                    balance += 1
                elif s[i] == ")":
                    if balance == 0:
                        return False
                    balance -= 1
            return not balance

        visited = set([s])
        queue = deque([s])
        res = set()
        while queue:
            changed = False
            for i in range(len(queue)):
                out = queue.popleft()
                visited.add(out)
                if valid(out):
                    res.add(out)
                    changed = True
                for i in range(len(out)):
                    if out[i] in '()':
                        rest = out[:i] + out[i+1:]
                        if rest not in visited:
                            queue.append(rest)
                            visited.add(rest)
            if changed:
                break
        
        return list(res)