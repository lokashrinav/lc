class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        carry = 0
        res = []
        i, j = len(arr1) - 1, len(arr2) - 1

        while (i >= 0 or j >= 0) or carry != 0:
            total = carry
            if i >= 0:
                total += arr1[i]
                i -= 1
            if j >= 0:
                total += arr2[j]
                j -= 1
            
            res.append(total & 1)
            carry = -(total // 2)

        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        return res[::-1]
