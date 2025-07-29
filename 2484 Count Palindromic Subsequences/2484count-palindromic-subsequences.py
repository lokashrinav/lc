class Solution:
    def countPalindromes(self, s: str) -> int:
        
        visited = defaultdict(int)
        before = defaultdict(int)
        hmap = defaultdict(int)
        next1 = Counter(s)

        for i in range(len(s)):
            for elem in visited:
                hmap[elem + s[i]] += visited[elem]
            visited[s[i]] += 1
        
        visited = defaultdict(int)
        total = 0
        for i in range(len(s)):
            # print(before, hmap, next1)
            next1[s[i]] -= 1
            for p in range(10):
                if s[i] + str(p) in hmap:
                    hmap[s[i] + str(p)] -= (next1[str(p)])
                    if hmap[s[i] + str(p)] == 0:
                        del hmap[s[i] + str(p)]

            for elem in before:
                total = (total + before[elem] * hmap[elem[::-1]]) % (10 ** 9 + 7) 

            for elem in visited:
                before[elem + s[i]] += visited[elem]

            visited[s[i]] += 1
        
        return total
            

            


            


        