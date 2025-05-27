class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # for a 10, we need at least 1 5, for a 20, we need at least 3 5s or 1 5 and 1 10


        arr = [0, 0, 0]
        for bill in bills:
            if bill == 10:
                if arr[0] == 0:
                    return False
                arr[1] += 1
                arr[0] -= 1
            elif bill == 20:
                if arr[0] >= 1 and arr[1] >= 1:
                    arr[0] -= 1
                    arr[1] -= 1
                elif arr[0] >= 3:
                    arr[0] -= 3
                else:
                    return False
            else:
                arr[0] += 1
        return True
        
