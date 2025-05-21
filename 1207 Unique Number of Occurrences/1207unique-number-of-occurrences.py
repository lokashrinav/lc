class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        hmap = Counter(arr)

        hset = set(hmap.values())

        return len(hset) == len(hmap)
        