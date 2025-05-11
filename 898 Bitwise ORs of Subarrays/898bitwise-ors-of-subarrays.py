class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        curr = set()

        for x in arr:
            curr = {x} | {x | v for v in curr}
            res |= curr
        
        return len(res)


        