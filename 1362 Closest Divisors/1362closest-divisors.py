class Solution:
    def closestDivisors(self, num: int) -> List[int]:

        def fun(num):
            curr = None
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    if curr is None or abs(curr[1] - curr[0]) > abs(num // i - i):
                        curr = [i, num // i]
            return curr
        
        first = fun(num + 1)
        second = fun(num + 2)

        return first if abs(first[1] - first[0]) < abs(second[1] - second[0]) else second

        
        