class Solution:
    def intToRoman(self, num: int) -> str:
        res = [[1, 'I'], [4, 'IV'], [5, 'V'], [9, 'IX'], [10, 'X'], 
        [40, 'XL'], [50, 'L'], [90, 'XC'], [100, 'C'], 
        [400, 'CD'], [500, 'D'], [900, 'CM'], [1000, 'M']]
        
        new_str = []
        rem = 0
        for i in range(len(res) - 1, -1, -1):
            # print(num, rem)
            if num >= res[i][0]:
                rem = num % res[i][0]
                num //= res[i][0]
                new_str += (res[i][1] * num)
                num = rem
    
        return ''.join(new_str)

