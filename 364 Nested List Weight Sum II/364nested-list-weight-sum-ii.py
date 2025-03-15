# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        def check(num, depth):
            if num.isInteger():
                maxDepth[0] = max(maxDepth[0], depth)
                return

            for elem in num.getList():
                check(elem, depth + 1)

        maxDepth = [0]
        for elem in nestedList:
            check(elem, 1)

        def dfs(num, depth):
            if num.isInteger():
                return (maxDepth[0] - depth + 1) * num.getInteger()
            
            total = 0
            for elem in num.getList():
                total += dfs(elem, depth + 1)
            
            return total

        total = 0
        for elem in nestedList:
            total += dfs(elem, 1)
        
        return total
        
