class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(node1, node2):
            dummy = ListNode(0)
            curr = dummy
            while node1 and node2:
                if node1.val > node2.val:
                    curr.next = node2
                    node2 = node2.next
                else:
                    curr.next = node1
                    node1 = node1.next
                curr = curr.next
            if node1:
                curr.next = node1
            elif node2:
                curr.next = node2
            return dummy.next

        def mergeList(node):
            if node and node.next:
                turtle, hare = node, node.next
                while hare and hare.next:
                    hare = hare.next.next
                    turtle = turtle.next
                saved = turtle.next
                turtle.next = None
                lis1 = mergeList(node)
                lis2 = mergeList(saved)
                return merge(lis1, lis2)
            return node

        return mergeList(head)

        

        