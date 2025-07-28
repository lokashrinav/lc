# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

        # 1, 2, #, #, 3, 4, #, #, 5, #, #
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = data.split(",")

        def dfs(ind):
            if ind >= len(data):
                return (None, ind + 1)
            elif data[ind] == "#":
                return (None, ind)

            root = TreeNode(int(data[ind]))

            left, ind1 = dfs(ind + 1)
            right, ind2 = dfs(ind1 + 1)

            root.left = left
            root.right = right

            return (root, ind2)

        return dfs(0)[0]

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))