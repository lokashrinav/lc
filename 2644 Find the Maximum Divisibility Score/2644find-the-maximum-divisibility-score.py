class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        maxNum = -1
        saved = None
        
        for elem in divisors:
            count = 0
            for elem2 in nums:
                if elem2 % elem == 0:
                    count += 1

            if count > maxNum:
                saved = elem
                maxNum = count
            elif count == maxNum:
                saved = min(saved, elem)
        
        return saved
        