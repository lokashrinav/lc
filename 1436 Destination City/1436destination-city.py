class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        hset = set()

        for y, x in paths:
            hset.add(y)
            hset.add(x)
        
        for y, x in paths:
            if y in hset:
                hset.remove(y)
        
        return list(hset)[0]
