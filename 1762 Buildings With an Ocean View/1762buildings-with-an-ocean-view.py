class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        minSoFar = float('-inf')
        lis = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > minSoFar:
                minSoFar = heights[i]
                lis.append(i)
        
        return lis[::-1]


