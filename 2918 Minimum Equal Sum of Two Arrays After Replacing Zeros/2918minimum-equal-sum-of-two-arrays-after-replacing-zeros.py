class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        6 - 11
        2 - 1

        8 - 12
        '''

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        count1 = nums1.count(0)
        count2 = nums2.count(0)

        if (count1 == 0 and sum1 < sum2 + count2) or (count2 == 0 and sum2 < sum1 + count1):
            return -1

        return max(count1 + sum1, count2 + sum2)