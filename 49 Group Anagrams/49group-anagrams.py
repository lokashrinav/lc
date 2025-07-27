class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)

        for elem in strs:
            hmap[tuple(sorted(list(elem)))].append(elem)
        
        return list(hmap.values())