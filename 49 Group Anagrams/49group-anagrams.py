class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)
        for str1 in strs:
            hmap[tuple(sorted(str1))].append(str1)
        
        return list(hmap.values())
