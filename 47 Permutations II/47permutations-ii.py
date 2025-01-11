import itertools
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter_list = Counter(nums)

        def dfs(hmap):
            if len(hmap) == 0:
                return [[]]
            
            permutations = []

            for key, val in list(hmap.items()):
                current = key
                hmap[key] -= 1
                if val == 1:
                    del hmap[key]
                for p in dfs(hmap):
                    permutations.append([key] + p)
                hmap[key] = hmap.get(key, 0) + 1

            return permutations
        
        return dfs(counter_list)
        
        