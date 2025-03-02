class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        # 1, 8, 6, 9, 0
        # palindrome of these numbers, 6 = 9
        nums = ['1', '8', '6', '9', '0']
        hmap = {'1': '1', '8':'8', '0':'0', '6':'9', '9':'6'}
        res = []
        
        if n == 1:
            return ['0', '1', '8']

        count = n
        def dfs(curr):
            if len(curr) == ((count + 1) // 2):
                new = curr[::]
                if (count % 2 and curr[-1] in '69') or curr[0] == '0':
                    return
                
                fun = len(new) if count % 2 == 0 else len(new) - 1

                for i in range(1, ((count // 2) + 1)):
                    new.append(hmap[curr[fun - i]])

                res.append(''.join(new))

                return
            
            if len(curr) >= ((count + 1) // 2):
                return
            
            for num in nums:
                curr.append(num)
                dfs(curr)
                curr.pop()
            
            return        

        dfs([])

        return res