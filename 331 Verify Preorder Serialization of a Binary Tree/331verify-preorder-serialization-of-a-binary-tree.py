class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        def pre(preorder):
            if not preorder:
                return (0, False)

            root = preorder[0]
            if root == '#':
                return (1, True)
                
            length, idk1 = pre(preorder[1:])
            length2, idk2 = pre(preorder[length+1:])

            return (1 + length + length2, idk1 and idk2)
        
        preorder = preorder.split(",")

        length, idk = pre(preorder)

        return idk and length == len(preorder)



        