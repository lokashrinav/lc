class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        include = 0
        total = 0
        l, m = 0, 0
        for i in range(len(nums)):
            include += 1 if nums[i] % 2 else 0
            
            while include > k:
                if nums[l] % 2:
                    include -= 1
                l += 1
            m = l

            if include == k:
                while not nums[m] % 2:
                    m += 1
                total += (m - l) + 1

        return total


        