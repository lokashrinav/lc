class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        2, 1, 2, 1
        1, 2, 1, 2

        1, -1, 1, -1

        -1, -1, 1, 1


        '''

        new = []
        for i in range(len(nums1)):
            new.append(nums1[i] - nums2[i])
    
        new.sort()
        count = sum(1 if elem > 0 else 0 for elem in new)
        total = count * (count - 1) // 2

        for elem in new:
            if elem < 0:
                ind = bisect_right(new, abs(elem))
                total += len(new) - ind
        
        total += count * new.count(0)

        return total