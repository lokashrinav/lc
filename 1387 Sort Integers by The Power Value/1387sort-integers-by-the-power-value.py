class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        
        def dfs(num):
            if num in cache:
                return cache[num]
            
            if num == 1:
                cache[num] = 0
                return 0
            
            calc = None
            if num % 2 == 0:
                calc = 1 + dfs(num // 2)
            else:
                calc = 1 + dfs(num * 3 + 1)

            cache[num] = calc

            return calc

        cache = {}
        for i in range(lo, hi + 1):
            if i not in cache:
                dfs(i)
        
        res = [i for i in range(lo, hi + 1)]

        def func(a, b):
            if cache[a] > cache[b]:
                return 1
            elif cache[b] > cache[a]:
                return -1
            else:
                return 1 if a > b else -1

        res.sort(key=cmp_to_key(func))

        return res[k - 1]


        