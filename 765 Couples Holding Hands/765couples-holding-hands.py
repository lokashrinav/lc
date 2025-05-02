class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:

        hmap = {}
        for i in range(len(row)):
            hmap[row[i]] = i // 2
        
        '''
        1, 3, 2, 7, 5, 6, 4, 0

        0 -> 3
        1 -> 0
        2 -> 1
        3 -> 2

        1, 0, 2, 7, 5, 6, 4, 3
        1, 0, 2, 5, 7, 6, 4, 3
        1, 0, 4, 5, 7, 6, 2, 3
        '''
        
        hmap2 = defaultdict(set)

        for i in range(len(row)):
            diff = 1 if row[i] % 2 == 0 else -1
            hmap2[hmap[row[i]]].add(hmap[row[i] + diff])


        def dfs(num, val, prev):
            #print(num, val, prev)

            if num in visited:
                return val - visited[num] - 1
            
            maxNum = 0
            visited[num] = val

            for elem in hmap2[num]:
                if elem == prev and len(hmap2[num]) != 1:
                    continue
                maxNum = max(dfs(elem, val + 1, num), maxNum)
            
            return maxNum

        visited = {}
        maxNum = 0

        '''
        0 -> 1
        1 -> 0
        '''

        total = 0
        for i in range(len(row) // 2):
            if i in visited:
                continue
            calc = dfs(i, 0, None)
            total += calc

        return total



            
            



