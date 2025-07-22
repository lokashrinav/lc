class Solution:
    def digitCount(self, num: str) -> bool:
        
        lnum = list(int(n) for n in num)
        hmap = Counter(lnum)

        flag = True
        for i in range(len(lnum)):
            if lnum[i] != hmap[i]:
                flag = False
                #print(hmap[i], i)
        
        return flag
