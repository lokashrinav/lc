class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        hset = set()
        hmap = defaultdict(int)
        maxCount = 0
        for student, bench in students:
            idk = (student, bench)
            if idk in hset:
                continue
            hmap[bench] += 1
            maxCount = max(hmap[bench], maxCount)
            hset.add(idk)
        
        return maxCount