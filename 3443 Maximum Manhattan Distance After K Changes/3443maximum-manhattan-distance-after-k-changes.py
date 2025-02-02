class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        idk = 'NSWE'
        op = {'N':'S', 'W':'E', 'S':'N', 'E':'W'}
        hmap = Counter(s)
        
        for i in idk:
            if i not in hmap:
                hmap[i] = 0
                
        fun1 = abs(hmap['N'] - hmap['S'])
        fun2 = abs(hmap['W'] - hmap['E'])  
        
        count = fun1 + fun2
        
        for i in range(len(idk)):
            hmap = Counter(s)
            for p in idk:
                if p not in hmap:
                    hmap[p] = 0
            if k > hmap[idk[i]]:
                count = hmap[idk[i]]
                hmap[idk[i]] = 0
                x = op[idk[i]]
                hmap[x] += count
            else:
                hmap[idk[i]] -= k
                hmap[op[idk[i]]] += k

            fun1 = abs(hmap['N'] - hmap['S'])
            fun2 = abs(hmap['W'] - hmap['E'])                 
                
            count = max(count, fun1 + fun2)

        for i in range(len(idk)):
            for p in range(i + 1, len(idk)):
                hmap = Counter(s)
                for z in idk:
                    if z not in hmap:
                        hmap[z] = 0
                total = 0
                free = k
                first, second = idk[i], idk[p]
                if op[first] == second:
                    continue
                #print(hmap, free)
                hmap2 = defaultdict(int)
                for z in range(len(s)):
                    if s[z] == first or s[z] == second:
                        if free:
                            hmap2[op[s[z]]] += 1      
                            free -= 1
                        else:
                            hmap2[s[z]] += 1
                    else:
                        hmap2[s[z]] += 1
                    fun1 = abs(hmap2['N'] - hmap2['S'])
                    fun2 = abs(hmap2['W'] - hmap2['E'])                 
                    #print(first, second, hmap2)
                    count = max(count, fun1 + fun2)
                #print(fun1, fun2, end='\n')
                #print("")

        print(count)
        return count