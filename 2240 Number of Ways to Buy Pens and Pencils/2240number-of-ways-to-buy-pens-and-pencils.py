class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:


        new = 0
        for i in range(total // cost1 + 1):
            curr = total - cost1 * i
            count = curr // cost2
            # print(i, count)
            new += count + 1
        
        return new





        '''

        x | _ 

        1 -> 2
        2



        '''