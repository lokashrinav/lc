# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        v1 = rand7()
        v2 = rand7()
        while v1 > 5: 
            v1 = rand7()
        
        while v2 == 7:
            v2 = rand7()
        
        if v2 > 3:
            return v1 + 5
        else:
            return v1

        

        