# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:                       # empty pattern is always a subtree
            return True
        if not root:                          # non-empty pattern, but empty big tree
            return False

        # ------------- constants for the two polynomial hashes -------------
        MOD1, MOD2  = 1_000_000_007, 1_000_000_009
        A1, B1, C1  = 911382323, 972663749, 972663053
        A2, B2, C2  =  97266367, 911382323,  97266353
        NULL_H1, NULL_H2 = 3, 7                # fingerprints of a null child

        # ------------ helper to combine hashes of a parent -----------------
        def combine(val, l1, r1, l2, r2, sz_left, sz_right):
            h1 = (val * A1 + l1 * B1 + r1 * C1 + 17) % MOD1
            h2 = (val * A2 + l2 * B2 + r2 * C2 + 23) % MOD2
            return h1, h2, 1 + sz_left + sz_right

        # ------------ hash (and size) of the pattern tree ------------------
        # this small DFS is only on the pattern; replace by Morris if you
        # *must* eliminate the recursion stack completely
        def hash_pattern(node):
            if not node:
                return NULL_H1, NULL_H2, 0
            lh1, lh2, ls = hash_pattern(node.left)
            rh1, rh2, rs = hash_pattern(node.right)
            return combine(node.val, lh1, rh1, lh2, rh2, ls, rs)

        pat_h1, pat_h2, pat_sz = hash_pattern(subRoot)

        # ---------------- Morris post-order on the big tree ----------------
        dummy = TreeNode(0)
        dummy.left = root
        cur, found = dummy, False

        # reverse the "right-spine" of a path; used by Morris post-order
        def reverse_path(start: TreeNode):
            prev, node = None, start
            while node:
                nxt = node.right
                node.right = prev
                prev, node = node, nxt
            return prev  # new head

        # process every node on the (now) right-spine from 'frm' down to 'to'
        def process_reverse(frm: TreeNode, to: TreeNode):
            nonlocal found
            tail = reverse_path(frm)
            node = tail
            while True:
                # extract previously stored child fingerprints (or NULL)
                if node.left:
                    lh1, lh2, ls = node.left.val if isinstance(node.left.val, tuple) else (NULL_H1, NULL_H2, 0)
                else:
                    lh1, lh2, ls = NULL_H1, NULL_H2, 0
                if node.right:
                    rh1, rh2, rs = node.right.val if isinstance(node.right.val, tuple) else (NULL_H1, NULL_H2, 0)
                else:
                    rh1, rh2, rs = NULL_H1, NULL_H2, 0

                # compute this node's own fingerprint & subtree size
                h1, h2, sz = combine(node.val if not isinstance(node.val, tuple) else node.val[0],
                                      lh1, rh1, lh2, rh2, ls, rs)

                # store tuple in-place (overwriting the original int)
                node.val = (h1, h2, sz)

                # match check
                if sz == pat_sz and h1 == pat_h1 and h2 == pat_h2:
                    found = True

                if node is to:
                    break
                node = node.right
            reverse_path(tail)  # restore the path

        while cur and not found:
            if not cur.left:
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right
                if not pred.right:            # first visit – create thread
                    pred.right = cur
                    cur = cur.left
                else:                         # second visit – thread exists
                    pred.right = None
                    process_reverse(cur.left, pred)  # all nodes on this edge are post-ordered
                    cur = cur.right

        return found