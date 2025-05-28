class Solution:
    def reformatNumber(self, number: str) -> str:

        res = deque()

        for elem in number:
            if elem.isdigit():
                res.append(elem)
        
        final = ""

        while len(res) > 4:
            final += res.popleft() + res.popleft() + res.popleft() + "-"
        
        if len(res) == 2:
            final += res.popleft() + res.popleft()
        elif len(res) == 3:
            final += res.popleft() + res.popleft() + res.popleft()
        elif len(res) == 4:
            final += res.popleft() + res.popleft() + "-" + res.popleft() + res.popleft()
        
        return final

        
        

        