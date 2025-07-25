# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        str1 = []
        def dfs(node):
            if not node:
                str1.append("N%")
                return
            
            str1.append(str(node.val) + "%")
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        if str1[-1] == "%":
            str1 = str1[:-1]

        return ''.join(str1)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        arr = data.split("%")

        def dfs(ind):
            
            if ind >= len(arr):
                return (None, ind)

            if arr[ind] == "N":
                return (None, ind)
            
            node = TreeNode(arr[ind]) 
            val, ind1 = dfs(ind + 1)
            node.left = val
            val, ind2 = dfs(ind1 + 1)
            node.right = val
            return (node, ind2)

        calc = dfs(0)
        return calc[0]

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans