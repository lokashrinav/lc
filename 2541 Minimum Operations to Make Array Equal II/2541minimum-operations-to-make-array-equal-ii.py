class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''
        [4,3,1,4]
        [1,3,7,1]

        -1, 0, 2, -1
        '''

        if k == 0:
            return -1 if nums1 != nums2 else 0

        total = 0
        count = 0
        for i in range(len(nums1)):
            diff = nums1[i] - nums2[i]
            if abs(nums1[i] - nums2[i]) % k != 0:
                return -1
            
            total += diff / k
            count += abs(diff) / k
            print(total, count)
        
        return -1 if total != 0 else int(count) // 2

        