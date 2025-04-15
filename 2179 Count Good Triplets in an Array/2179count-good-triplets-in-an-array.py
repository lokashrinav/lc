class BinaryIndexedTree:
    # Initialization of the binary indexed tree with given size n.
    def __init__(self, size):
        self.size = size
        self.tree_array = [0] * (size + 1)

    # Calculate the least significant bit that is set (i.e., lowest power of 2 that divides x).
    @staticmethod
    def lowbit(x):
        return x & -x

    # Update the binary indexed tree by adding `delta` to index `index`.
    def update(self, index, delta):
        while index <= self.size:
            self.tree_array[index] += delta
            index += BinaryIndexedTree.lowbit(index)

    # Compute the prefix sum from the start to index `index`.
    def query(self, index):
        sum_value = 0
        while index > 0:
            sum_value += self.tree_array[index]
            index -= BinaryIndexedTree.lowbit(index)
        return sum_value


class Solution:
    # Function to count the number of "good triplets" in the permutation of nums1 that satisfy the condition
    # in the problem statement, using nums2 to determine the ideal order.
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Build a position mapping of elements in nums2 for O(1) lookup.
        position = {value: index for index, value in enumerate(nums2, 1)}
        good_triplets_count = 0  # Initialize counter for good triplets
        length = len(nums1)  # The length of nums1 and nums2 arrays
        tree = BinaryIndexedTree(length)  # Instantiate a Binary Indexed Tree

        # Process each number in nums1 to count the number of good triplets.
        for number in nums1:
            order = position[number]  # Find the position of the current number in nums2
            left_count = tree.query(order)  # Count of numbers before the current number's ideal position
            # Count of numbers after the current number by subtracting the counts obtained from the tree
            right_count = length - order - (tree.query(length) - tree.query(order))
            # Increment the count of good triplets by the product of left and right counts
            good_triplets_count += left_count * right_count
            # Update the Binary Indexed Tree with the current number's position
            tree.update(order, 1)

        return good_triplets_count  # Return the total count of good triplets