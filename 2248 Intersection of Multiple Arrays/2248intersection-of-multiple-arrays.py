class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        prev = nums[0]
        for i in range(1, len(nums)):
            set1 = set(prev)
            set2 = set(nums[i])

            intersection_set = set1.intersection(set2)

            prev = list(intersection_set)
        
        return sorted(prev)
        