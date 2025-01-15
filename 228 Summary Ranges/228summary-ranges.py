class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        first = str(nums[0])
        last = str(nums[0])
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                last = str(nums[i + 1])
            else:
                if first != last:
                    str1 = first + "->" + last
                else:
                    str1 = first
                res.append(str1)
                first = str(nums[i + 1])
                last = str(nums[i + 1])
        
        if first != last:
            str1 = first + "->" + last
        else:
            str1 = first
        
        res.append(str1)

        return res

        