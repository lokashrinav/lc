class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        num_to_group = {}

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(n)
            num_to_group[n] = len(groups) - 1
        
        res = []

        for num in nums:
            j = num_to_group[num]
            res.append(groups[j].popleft())
            
        return res

        # [1, 2, 3], [5, 6]


    
