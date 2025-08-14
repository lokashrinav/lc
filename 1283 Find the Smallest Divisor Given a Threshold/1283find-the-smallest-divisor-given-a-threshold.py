class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, 10 * max(nums)
        saved = 10 * max(nums)

        while l <= r:
            # nonlocal saved
            m = (l + r) // 2
            curr = nums.copy()
            for i in range(len(curr)):
                curr[i] = ceil(curr[i] / m)

            if sum(curr) <= threshold:
                saved = min(saved, m)
                r = m - 1
            else:
                l = m + 1
                    
        return saved

        