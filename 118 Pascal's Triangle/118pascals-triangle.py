class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        final = []
        if numRows == 1:
            return [[1]]

        curr = [1, 1]
        final.append([1])
        final.append(curr)

        for i in range(2, numRows):
            res = []
            res.append(curr[0])
            for i in range(len(curr) - 1):
                res.append(curr[i] + curr[i + 1])

            res.append(curr[0])
            final.append(res)
            curr = res

        return final
        