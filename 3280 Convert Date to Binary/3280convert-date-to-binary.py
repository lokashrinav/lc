class Solution:
    def convertDateToBinary(self, date: str) -> str:

        date = date.split("-")

        res = []

        for elem in date:
            print()
            res.append(str(bin(int(elem)))[2:])
        
        return '-'.join(res)

        