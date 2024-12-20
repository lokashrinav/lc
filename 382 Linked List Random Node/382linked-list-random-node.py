# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.link = head

    def getRandom(self) -> int:
        reservoir = -1
        current = self.link
        index = 0

        while current:
            if random.randint(0, index) == 0:
                reservoir = current.val
            current = current.next
            index += 1
        
        return reservoir
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()