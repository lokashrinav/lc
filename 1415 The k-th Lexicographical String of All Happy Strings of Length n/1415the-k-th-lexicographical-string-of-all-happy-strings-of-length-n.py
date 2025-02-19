class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        alp = ['a', 'b', 'c']
        kth = [1]
        saved = [""]

        def dfs(curr):
            if len(curr) == n:
                print(kth[0], curr)
                if kth[0] == k:
                    saved[0] = curr
                    return True
                else:
                    kth[0] += 1
                return False

            for char in alp:
                if curr[-1] != char:
                    if dfs(curr + char):
                        return True
            
            return False
        
        for char in alp:
            if dfs(char):
                return saved[0]
        
        return saved[0]
        

        