class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # startValue * (2 ** x) > target
        # log2(target) = x
        # 
        
        total = 0
        while target > startValue:
            if target % 2 == 0:
                target = target // 2
            else:
                target += 1
            total += 1
        total += startValue - target
        return total