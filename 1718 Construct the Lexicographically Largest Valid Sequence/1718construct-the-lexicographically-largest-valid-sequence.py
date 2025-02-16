class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 1 + 2 * (n - 1)
        sol = [0] * (length)
        used = set()

        def dfs(ind):
            if ind == length:
                return True

            if sol[ind] != 0:
                return dfs(ind + 1)
            
            for i in range(n, 1, -1):
                if i not in used and (ind + i < length) and sol[ind] == 0 and sol[ind + i] == 0:
                    used.add(i)
                    sol[ind] = i
                    sol[ind + i] = i

                    if dfs(ind + 1):
                        return True
                    
                    sol[ind] = 0
                    sol[ind + i] = 0
                    used.remove(i)
                
            if 1 not in used:
                sol[ind] = 1
                used.add(1)

                if dfs(ind + 1):
                    return True
                
                sol[ind] = 0
                used.remove(1)
        
            return False          

        dfs(0)
        return sol