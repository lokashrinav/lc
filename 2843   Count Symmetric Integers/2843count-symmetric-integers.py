class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count = 0
        while low <= high:
            print(low)
            str_length = len(str(low))
            if str_length % 2 == 0:
                mid = str_length // 2
                if sum(int(d) for d in str(low)[:mid]) == sum(int(d) for d in str(low)[mid:]):
                    count += 1
                low += 1
            else:
                low = 10 ** str_length

        
        return count
