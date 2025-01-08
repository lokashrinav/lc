class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                xy += 1
            elif s2[i] == 'x' and s1[i] == 'y':
                yx += 1
        
        if (xy + yx) % 2 == 1:
            return -1
        
        count = (xy // 2) + (yx // 2)

        if xy % 2 and yx % 2:
            return count + 2

        return count