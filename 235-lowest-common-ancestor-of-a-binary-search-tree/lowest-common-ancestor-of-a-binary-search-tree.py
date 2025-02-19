class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root  # Start traversal from the root.

        while cur:
            if p.val > cur.val and q.val > cur.val:  # Both nodes are in the right subtree.
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:  # Both nodes are in the left subtree.
                cur = cur.left
            else:
                return cur  # Found the LCA (either a split point or one of the nodes).
