class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        # Create a stack to hold nodes and initialize depth and value variables.
        nodes_stack = []
        current_depth = 0
        current_value = 0

        # Loop through each character in the traversal string.
        for i in range(len(traversal)):
            if traversal[i] == '-':
                # Increment the depth for every '-' character encountered.
                current_depth += 1
            else:
                # Calculate the node's value.
                current_value = 10 * current_value + (ord(traversal[i]) - ord('0'))

            # Check for the end of number or end of string.
            if i + 1 == len(traversal) or (traversal[i].isdigit() and traversal[i + 1] == '-'):
                # Create a new node with the computed value.
                new_node = TreeNode(current_value)

                # If the stack size is greater than the current depth, pop until the sizes match.
                while len(nodes_stack) > current_depth:
                    nodes_stack.pop()

                # If the stack is not empty, assign the new node to the appropriate child of the top node.
                if nodes_stack:
                    if nodes_stack[-1].left is None:
                        nodes_stack[-1].left = new_node
                    else:
                        nodes_stack[-1].right = new_node

                # Push the new node onto the stack.
                nodes_stack.append(new_node)

                # Reset current depth and value for the next node.
                current_depth = 0
                current_value = 0
      
        # The result is the root of the tree. It's the bottommost node in the stack.
        result = None
        while nodes_stack:
            result = nodes_stack.pop()

        # Return the reconstructed binary tree.
        return result