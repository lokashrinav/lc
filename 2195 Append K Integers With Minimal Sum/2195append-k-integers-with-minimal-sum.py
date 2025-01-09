class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        prev = 0
        total = 0
        count = 0
        for i in range(len(nums)):
            if count >= k:
                break
            missing = nums[i] - prev - 1
            if missing > 0:
                take = min(missing, k - count)
                end = prev + take
                total += (end * (end + 1)) // 2 - (prev * (prev + 1)) // 2
                count += take
                if count == k:
                    break
            prev = nums[i]
        
        if count < k:
            end = prev + (k - count)
            total += (end * (end + 1)) // 2 - (prev * (prev + 1)) // 2
    
        return total
