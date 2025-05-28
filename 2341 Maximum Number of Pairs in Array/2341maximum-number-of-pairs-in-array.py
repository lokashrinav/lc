class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
    
        hmap = Counter(nums)

        count = 0
        first = 0
        for key, val in hmap.items():
            if val % 2:
                count += 1
            
            first += val // 2
        
        return [first, count]