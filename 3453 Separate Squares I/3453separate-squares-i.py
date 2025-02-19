class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(li * li for _, y, li in squares)
        target = total_area / 2.0

        low = min(y for _, y, li in squares)
        high = max(y + li for _, y, li in squares)

        tol = 1e-6
        while high - low > tol:
            mid = (low + high) / 2.0
            below_area = 0.0

            for x, y, li in squares:
                if mid <= y:
                    area = 0.0
                elif mid >= y + li:
                    area = li * li
                else:
                    area = (mid - y) * li
                below_area += area

            if below_area < target:
                low = mid
            else:
                high = mid

        return low
