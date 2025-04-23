class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        hmap = defaultdict(int)
        hmap2 = defaultdict(int)

        for i in range(1, n + 1):
            total = 0
            for elem in str(i):
                total += int(elem)
            hmap2[total] += 1
        
        print(hmap2)

        for key, val in hmap2.items():
            hmap[val] += 1
        
        print(hmap)
        
        return hmap[max(hmap.keys())]
