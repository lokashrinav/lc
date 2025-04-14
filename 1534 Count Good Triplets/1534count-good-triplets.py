class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def countInRange(sorted_list: List[int], lower_bound: int, upper_bound: int) -> int:
            left_index = bisect.bisect_left(sorted_list, lower_bound)
            right_index = bisect.bisect_right(sorted_list, upper_bound)
            return right_index - left_index
        
        count = 0
        n = len(arr)
        for j in range(1, n - 1):
            leftList = [arr[i] for i in range(j) if abs(arr[i] - arr[j]) <= a]
            rightList = [arr[k] for k in range(j + 1, n) if abs(arr[j] - arr[k]) <= b]
            rightList.sort()
            for x in leftList:
                lower_bound = max(arr[j] - b, x - c)
                upper_bound = min(arr[j] + b, x + c)
                count += countInRange(rightList, lower_bound, upper_bound)
                
        return count