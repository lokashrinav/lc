class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        weight.sort()
        total = 0
        count = 0
        for i in range(len(weight)):
            if total + weight[i] > 5000:
                return count
            total += weight[i]
            count += 1

        return count