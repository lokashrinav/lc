# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        
        p1, p2 = poly1, poly2

        head = node = PolyNode(0, 0, None)

        while p1 or p2:
            if not p1:
                curr1 = 0
                curr2 = p2.coefficient
                power = p2.power
                p2 = p2.next
            elif not p2:
                curr2 = 0
                curr1 = p1.coefficient
                power = p1.power
                p1 = p1.next
            elif p1.power > p2.power:
                curr2 = 0
                curr1 = p1.coefficient
                power = p1.power
                p1 = p1.next
            elif p2.power > p1.power:
                curr1 = 0
                curr2 = p2.coefficient
                power = p2.power
                p2 = p2.next
            else:
                curr2 = p2.coefficient
                curr1 = p1.coefficient
                power = p1.power
                p1 = p1.next
                p2 = p2.next
                
            if curr1 + curr2 == 0:
                continue
            node.next = PolyNode(curr1 + curr2, power, None)
            node = node.next
        
        return head.next
            

        