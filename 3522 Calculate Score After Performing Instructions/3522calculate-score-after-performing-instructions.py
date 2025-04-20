class Solution(object):
    def calculateScore(self, instructions, values):
        """
        :type instructions: List[str]
        :type values: List[int]
        :rtype: int
        """
        i = 0
        hset = set()
        total = 0
        while len(values) > i >= 0:
             
            if i in hset:
                break
                
            hset.add(i)
            
            if instructions[i] == "add":
                total += values[i]
                i += 1
            else:
                i += values[i]
            
        

        return total

        