from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        # Perform in-order depth-first search to traverse the tree.
        def in_order_dfs(node):
            if node is None:
                return
          
            # Recurse on the left child.
            in_order_dfs(node.left)
          
            # Process the current node.
            # If we have fewer than k values, add current node's value.
            if len(closest_values) < k:
                closest_values.append(node.val)
            else:
                # Once we have k values, check if current node is closer to target
                # than the first value in the deque. If not, no need to proceed further.
                if abs(node.val - target) >= abs(closest_values[0] - target):
                    return
              
                # If the current node is closer, pop the first value and append the current value.
                closest_values.popleft()
                closest_values.append(node.val)
          
            # Recurse on the right child.
            in_order_dfs(node.right)

        # This deque will store the closest k values encountered so far.
        closest_values = deque()
      
        # Start the in-order traversal of the tree.
        in_order_dfs(root)
      
        # Return the k closest values as a list.
        return list(closest_values)