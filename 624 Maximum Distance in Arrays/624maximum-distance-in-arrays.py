class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        
        minSoFar = None
        maxSoFar = None

        maxDist = 0
        for i in range(len(arrays)):
            if i == 0:
                minSoFar = arrays[i][0]
                maxSoFar = arrays[i][-1]   
            else:
                idk = max(abs(arrays[i][-1] - minSoFar), abs(maxSoFar - arrays[i][0]))
                '''idk2 = max(abs(arrays[i][-1] - maxSoFar), abs(minSoFar - arrays[i][0]))
                idk3 = max(idk, idk2)'''
                maxDist = max(maxDist, idk)
                minSoFar = min(arrays[i][0], minSoFar)
                maxSoFar = max(maxSoFar, arrays[i][-1])

        return maxDist