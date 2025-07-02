class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum1 = sum(rolls)

        calc = mean * (len(rolls) + n) - sum1

        res = [1] * n

        calc -= n

        ind = 0

        while calc:
            #print(res)
            if res[ind] == 6:
                ind += 1

            if ind >= len(res):
                return []

            res[ind] += 1
            calc -= 1

        return res