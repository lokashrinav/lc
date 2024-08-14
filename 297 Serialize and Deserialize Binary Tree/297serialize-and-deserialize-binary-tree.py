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
        string = []
        def dfs(node):
            if not node:
                string.append("null")
                return
            string.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        result_string = ",".join(string)
        return result_string
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        arr = data.split(",")
        print(arr)
        i = [0]
        def dfs():
            if arr[i[0]] == "null":
                i[0] += 1
                return None
            node = TreeNode(int(arr[i[0]]))
            i[0] += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))