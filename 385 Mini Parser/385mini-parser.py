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
    def deserialize(self, s: str) -> NestedInteger:

        res = NestedInteger()
        def dfs(ind, arr):
            curr = ""
            while ind < len(s):
                if s[ind] == "]":
                    if curr:
                        arr.add(NestedInteger(int(curr)))
                    return ind + 1
                if s[ind] == "[":
                    first = NestedInteger()
                    i = dfs(ind + 1, first)
                    arr.add(first)
                    ind = i
                elif s[ind].isdigit() or s[ind] == "-":
                    curr += s[ind]
                    ind += 1        
                else:
                    if curr:
                        arr.add(NestedInteger(int(curr)))
                    curr = ""
                    ind += 1

            if curr:
                arr.add(NestedInteger(int(curr)))

        dfs(0, res)

        return res.getList()[0]


        