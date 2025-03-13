class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        ind = 0
        if a == 0:
            for i in range(len(nums)):
                nums[i] = nums[i] * b + c
            return nums if b >= 0 else nums[::-1]

        vertex = -b / (2 * a)
        for i in range(len(nums)):
            if nums[i] >= vertex:
                ind = i
                break

        first = nums[:ind]
        second = nums[ind:]

        res = []

        for i in range(len(first)):
            first[i] = (first[i] ** 2) * a + first[i] * b + c

        for i in range(len(second)):
            second[i] = (second[i] ** 2) * a + second[i] * b + c
        
        p1, p2 = 0, 0

        if first and first[0] > first[-1]:
            first = first[::-1]

        if second and second[0] > second[-1]:
            second = second[::-1]       

        if not first:
            return second
        elif not second:
            return first
        
        print(first, second)

        while p1 < len(first) or p2 < len(second):
            if p2 >= len(second):
                res.append(first[p1])
                p1 += 1
                continue
            if p1 >= len(first):
                res.append(second[p2])
                p2 += 1
                continue
            
            if first and second and first[p1] < second[p2]:
                res.append(first[p1])
                p1 += 1
            else:
                res.append(second[p2])
                p2 += 1
        
        return res
            

            
