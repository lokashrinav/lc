class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            res.append(chr(65 + (columnNumber % 26)))
            columnNumber //= 26
        
        print(res)
        return ''.join(res)[::-1]