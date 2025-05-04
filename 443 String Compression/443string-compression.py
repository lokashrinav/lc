class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        res = []
        prev = None
        total = 0
        
        for i in range(len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                if count > 1:
                    res.append(prev + str(count))
                elif count == 1:
                    res.append(prev)

                count = 1
                prev = chars[i]
        
        if count == 1:
            res.append(prev)
        else:
            res.append(prev + str(count))
        
        res = list(''.join(str(s) for s in res))

        print(res, chars)
        for i in range(len(res)):
            chars[i] = res[i]
            
        return len(res)
            
        