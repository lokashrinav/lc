class Solution:
    def isDecomposable(self, s: str) -> bool:
        three = 0
        two = 0
        for key, val in groupby(s):
            calc = len(list(val))
            if (calc - 2) % 3 == 0:
                three += calc // 3
                two += 1
            elif calc % 3 == 0:
                three += 1
            elif calc == 2:
                two += 1
            else:
                return False

        return two == 1