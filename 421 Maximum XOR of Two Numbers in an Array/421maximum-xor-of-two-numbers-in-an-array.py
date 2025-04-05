class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:     
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        maxBitLength = 1
        for i in range(len(nums)):
            maxBitLength = max(nums[i].bit_length(), maxBitLength)

        head = Node(0)

        for i in range(len(nums)):
            diff = maxBitLength - nums[i].bit_length()
            node = head
            num = nums[i]

            while diff:
                diff -= 1
                if node.left is None:
                    node.left = Node(0)
                node = node.left
                
            p = nums[i].bit_length() - 1
            while p >= 0:
                curr = (num >> p) & 1
                if curr:
                    if not node.right:
                        node.right = Node(1)
                    node = node.right
                else:
                    if not node.left:
                        node.left = Node(0)
                    node = node.left
                p -= 1


        def dfs(node, num, pos):
            if pos < 0:
                return ""
            bit = (num >> pos) & 1
            if bit == 0:
                if node.right:
                    return "1" + dfs(node.right, num, pos - 1)
                else:
                    return "0" + dfs(node.left, num, pos - 1)
            else:
                if node.left:
                    return "0" + dfs(node.left, num, pos - 1)
                else:
                    return "1" + dfs(node.right, num, pos - 1)

        maxNum = 0
        for i in range(len(nums)):
            calc = dfs(head, nums[i], maxBitLength - 1)
            red = int(calc, 2)
            print(calc, red)
            maxNum = max(nums[i] ^ red, maxNum)

        return maxNum
        

        