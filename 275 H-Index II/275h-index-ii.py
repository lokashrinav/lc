class Solution:
    def hIndex(self, citations: List[int]) -> int:

        l, r = 0, len(citations) - 1
        saved = 0

        while l <= r:
            m = (l + r) // 2
            if citations[m] < len(citations) - m:
                l = m + 1
            else:
                saved = len(citations) - m
                r = m - 1
        
        return saved

        