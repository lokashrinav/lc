class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        total = 0

        for elem in ["P", "G", "M"]:
            carry = 0

            total += garbage[0].count(elem)
            for i in range(1, len(garbage)):
                carry += travel[i - 1]
                if garbage[i].count(elem):
                    total += carry
                    total += garbage[i].count(elem)
                    carry = 0
        
        return total


            
        