class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        res1, res2 = [], []
        for i in range(len(nums)):
            if i % 2 == 0:
                res1.append(nums[i])
            else:
                res2.append(nums[i])
        
        res1.sort()
        res2.sort(reverse=True)

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = res1[i // 2]
            else:
                nums[i] = res2[i // 2]
        
        return nums


        
        