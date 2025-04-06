class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = [0] * len(nums)
        arr2 = [[] for i in range(len(nums))]

        for i in range(len(nums)):
            arr[i] = nums[i]
            arr2[i] = [nums[i]]
            for p in range(i):
                if nums[i] % arr[p] == 0 and 1 + len(arr2[p]) > len(arr2[i]):
                    arr[i] = lcm(nums[i], arr[p])
                    arr2[i] = [nums[i]] + arr2[p]
        print(arr)
        print(arr2)
        
        curr = []
        for i in range(len(nums)):
            if len(arr2[i]) > len(curr):
                curr = arr2[i]
        
        return curr


            
                            
