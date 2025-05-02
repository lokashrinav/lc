class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        

        def dfs(ind, prev1, prev2, curr, count):
            if ind == len(num):
                print(ind, prev1, prev2, curr, count)
                if count < 3:
                    return False
                return True if not curr else False
            
            idk = curr + num[ind]
            if len(idk) >= 2 and idk[0] == "0":
                return False

            if not prev1:                      
                if dfs(ind + 1, curr + num[ind], prev2, "", count + 1) or dfs(ind + 1, prev1, prev2, curr + num[ind], count):
                    return True
                return False
            
            if not prev2:
                if dfs(ind + 1, prev1, curr + num[ind], "", count + 1) or dfs(ind + 1, prev1, prev2, curr + num[ind], count):
                    return True
                return False

            if int(prev1) + int(prev2) == int(curr + num[ind]):
                if dfs(ind + 1, prev2, curr + num[ind], "", count + 1):
                    return True
                            
            return dfs(ind + 1, prev1, prev2, curr + num[ind], count)
        
        return dfs(0, "", "", "", 0)
            
            
