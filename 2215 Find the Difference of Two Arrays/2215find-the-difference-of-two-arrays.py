class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = []
        answer2 = []
        for elem in set1:
            if elem not in set2:
                answer1.append(elem)
            
        for elem in set2:
            if elem not in set1:
                answer2.append(elem)
        
        return [answer1, answer2]
        