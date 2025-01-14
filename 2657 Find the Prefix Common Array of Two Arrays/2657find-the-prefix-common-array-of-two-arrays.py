class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # [0, 1, 0, 0]
        # [0, 2, 0, 0]
        # [0, 2, 3, 0]
        # [0, 2, 3, 4]

        prefix = [0] * len(A)

        hmap = {}

        for i in range(len(B)):
            hmap[B[i]] = i

        for i in range(len(A)):
            maxNum = max(hmap[A[i]], i)
            prefix[maxNum] += 1
        
        for i in range(len(prefix) - 1):
            prefix[i + 1] += prefix[i]

        return prefix