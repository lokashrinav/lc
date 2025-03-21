class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def find_median(nums):
            return sorted(nums)[len(nums) // 2]

        def mapped_index(i):
            return (1 + 2 * i) % (len(nums) | 1)

        n = len(nums)
        median = find_median(nums)

        def hug(i):
            return (1 + 2 * i) % (n | 1)
        
        l, m, r = 0, 0, len(nums) - 1

        while m <= r:
            if nums[hug(m)] > median:
                nums[mapped_index(m)], nums[mapped_index(l)] = nums[mapped_index(l)], nums[mapped_index(m)]
                l += 1
                m += 1
            elif nums[hug(m)] < median:
                nums[mapped_index(m)], nums[mapped_index(r)] = nums[mapped_index(r)], nums[mapped_index(m)]
                r -= 1
            else:
                m += 1





        
