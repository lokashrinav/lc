# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        total = m
        directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]
        r, c, d = 0, 0, 0
        grid = [[-1] * n for i in range(m)]
        top, bottom, left, right = 0, m, 0, n
        while head:
            dx, dy = directions[d]
            while head and left <= c < right and top <= r < bottom and grid[r][c] == -1:
                grid[r][c] = head.val
                head = head.next
                r, c = r + dx, c + dy
                
            r, c = r - dx, c - dy
            d += 1
            d = d % 4
            dx, dy = directions[d]
            r, c = r + dx, c + dy

        return grid


