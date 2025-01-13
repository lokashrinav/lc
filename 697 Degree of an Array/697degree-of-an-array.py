class Solution:
    from collections import defaultdict
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        first = {}
        last = {}

        for i in range(len(nums)):
            freq[nums[i]] += 1
            if nums[i] not in first:
                first[nums[i]] = i
            last[nums[i]] = i
        
        degree = max(freq.values())

        minL = float('inf')

        for num in freq.keys():
            print(num)
            if freq[num] == degree:
                minL = min(last[num] - first[num] + 1, minL)

        return minL
        

