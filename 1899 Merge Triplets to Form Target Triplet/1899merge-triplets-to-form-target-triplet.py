class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # If it is not the smallest element
        bool1, bool2, bool3 = False, False, False
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            if triplets[i][0] == target[0]:
                bool1 = True
            if triplets[i][1] == target[1]:
                bool2 = True
            if triplets[i][2] == target[2]:
                bool3 = True
        if bool1 and bool2 and bool3:
            return True
        return False
        
        