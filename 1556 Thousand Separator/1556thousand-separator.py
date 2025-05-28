class Solution:
    def thousandSeparator(self, n: int) -> str:

        str_n = str(n)
        if len(str_n) < 4:
            return str_n
        
        queue = deque(list(str_n[::-1]))
        count = 0

        res = []
        while queue:
            out = queue.popleft()
            if count == 3:
                res.append(".")
                count = 0
            count += 1
            res.append(out)
        
        return ''.join(res)[::-1]



        