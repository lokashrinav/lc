class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        curr = 1
        res = []
        ind = 0
        
        while True:
            if ind == len(target):
                break
            if target[ind] == curr:
                curr += 1
                ind += 1
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
                curr += 1
        
        return res
        