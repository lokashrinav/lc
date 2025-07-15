class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        hmap = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        res = []
        def dfs(ind, curr):
            if ind == len(digits):
                res.append(curr)
                return 

            calc = digits[ind]
            val = hmap[int(calc)]
            for i in range(len(val)):
                dfs(ind + 1, curr + val[i])
        
        dfs(0, "")

        return res
        