class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        curr = [0]
        for i in range(len(differences)):
            curr.append(curr[-1] + differences[i])
        
        maxDiff = max(curr) - min(curr)

        calc = (upper - lower + 1)

        return max(0, calc - maxDiff)

        '''
        0, 3, -1, 4, 5, 3

        4

        '''