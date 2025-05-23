# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:

        node = head
        '''
        1 -> 2 -> 3
        '''

        res = []

        while node:
            res.append(node)
            node = node.getNext()
        
        for i in range(len(res) - 1, -1, -1):
            res[i].printValue()
        

        