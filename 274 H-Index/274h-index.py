class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0] * (len(citations) + 1)

        for i in range(len(citations)):
            if citations[i] >= len(citations):
                counts[-1] += 1
            else:
                counts[citations[i]] += 1 

        maxNum = 0
        num = 0
        print(counts)
        for i in range(len(citations), -1, -1):
            num += counts[i]
            if num >= i:
                return i

        return 0

        