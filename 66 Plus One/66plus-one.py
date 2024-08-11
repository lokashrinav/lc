class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        for i in digits:
            integer = integer * 10 + i
        
        integer += 1

        integer = str(integer)

        list1 = []

        for i in integer:
            list1.append(int(i))
        return list1

        
        