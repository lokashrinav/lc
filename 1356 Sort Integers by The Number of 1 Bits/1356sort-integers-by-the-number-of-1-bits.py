class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def func(a, b):
            if a.bit_count() == b.bit_count():
                if a > b:
                    return 1
                else:
                    return -1
            return 1 if a.bit_count() > b.bit_count() else -1

        arr = sorted(arr, key=cmp_to_key(func))

        return arr
        