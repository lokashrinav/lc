class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum1 = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                div = num / i
                sum1 += (i + div)
        
        return sum1 == num
            

        
        