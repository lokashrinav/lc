class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        add = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)

        if bx1 > ax2 or ax1 > bx2 or by1 > ay2 or ay1 > by2:
            return add

        left = max(ax1, bx1)

        right = min(bx2, ax2)

        down = max(ay1, by1)

        up = min(ay2, by2)

        sub = (right - left) * (up - down)

        return add - sub


        