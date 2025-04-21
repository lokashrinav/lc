class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        hset = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                hset.add(fronts[i])

        minNum = float('inf')
        for i in range(len(fronts)):
            if fronts[i] not in hset:
                minNum = min(minNum, fronts[i])
            if backs[i] not in hset:
                minNum = min(minNum, backs[i])
        
        return minNum if minNum != float('inf') else 0
        