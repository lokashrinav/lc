class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        def func(firstWord):
            first = ""

            for i in range(len(firstWord)):
                first += str((ord(firstWord[i]) - 97))
            
            return first
        
        return int(func(firstWord)) + int(func(secondWord)) == int(func(targetWord))
        


        