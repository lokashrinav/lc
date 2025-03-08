class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        '''
        
        equal number % 2 == 0 of count except 1

        '''

        if len(s) == 1:
            return [s]

        hmap = defaultdict(int)

        for char in s:
            hmap[char] += 1
        
        middle = ""
        count = 0
        for elem in hmap:
            if hmap[elem] % 2 == 1:
                count += 1
                middle = elem
                hmap[elem] -= 1
            if count > 1:
                return []
            hmap[elem] //= 2
        
        count = sum(hmap.values())
        res = []

        def dfs(arr):
            if len(arr) == count:
                if middle:
                    res.append(''.join(arr + [middle] + arr[::-1]))
                else:
                    res.append(''.join(arr + arr[::-1]))
                return
            
            for num in hmap:
                if hmap[num] > 0:
                    arr.append(num)
                    hmap[num] -= 1
                    dfs(arr)
                    arr.pop()
                    hmap[num] += 1
        
        dfs([])

        return res
            


        

        
        
