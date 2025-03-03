# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.arr = []
        if self.iterator.hasNext():
            self.arr.append(self.iterator.next())
        self.ind = 0
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.arr[self.ind]

    def next(self):
        """
        :rtype: int
        """
        saved = self.arr[self.ind]
        self.ind += 1
        if self.iterator.hasNext():
            self.arr.append(self.iterator.next())
        return saved

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.arr) != self.ind
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].