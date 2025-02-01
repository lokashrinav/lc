class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        l, r = 0, len(arr)

        while l < r:
            m = (l + r) // 2
            idk = arr[m] - (m + 1)

            if k <= idk:
                r = m
            else:
                l = m + 1
        
        return l + k

        
        # arr[l] - l - 1 shows how many numbers to the left of curr is

        