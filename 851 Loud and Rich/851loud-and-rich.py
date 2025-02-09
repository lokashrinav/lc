class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        adj = defaultdict(list)

        for i in range(len(richer)):
            first, second = richer[i]
            adj[second].append(first)
        
        cache = {}

        def dfs(num):
            if num in cache:
                return cache[num]
            
            minNum = quiet[num]
            minVal = num
            for num1 in adj[num]:
                num2, num3 = dfs(num1)
                if num2 < minNum:
                    minNum = num2
                    minVal = num3

            cache[num] = (minNum, minVal)

            return cache[num]

        res = []

        for i in range(len(quiet)):
            res.append(dfs(i)[1])
        
        return res

        