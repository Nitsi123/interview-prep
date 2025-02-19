from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Follow-up Questions:
        # 1. What if the tree is empty? (Assume `root` is always valid.)
        # 2. Can there be duplicate values in the tree? (Yes, all nodes are valid.)
        # 3. What if all nodes are negative? (Still works since we're comparing relative values.)
        # 4. What if the tree is skewed? (DFS handles any shape.)

        # Brute Force Approach:
        # - Perform a DFS traversal.
        # - For each node, compare it with all ancestor nodes to check if it's the max.
        # - This results in redundant comparisons.
        # - Time Complexity: O(n^2), since we traverse up the tree for each node.
        # - Space Complexity: O(h), where `h` is the tree height.

        # Optimized Approach (DFS with Maximum Tracking):
        # - **Instead of checking all ancestors**, pass the **maximum value** seen along the path.
        # - If `root.val >= max_so_far`, it's a **good node**.
        # - **Recursively update the max value** when traversing left and right subtrees.
        # - Time Complexity: O(n), since we visit each node once.
        # - Space Complexity: O(h), where `h` is the tree height (O(log n) for balanced, O(n) worst case).

        def helper(root, max_so_far):
            if root is None:
                return 0

            # A node is "good" if its value is greater than or equal to max_so_far.
            res = 1 if root.val >= max_so_far else 0

            # Update max_so_far for the subtree.
            max_so_far = max(max_so_far, root.val)

            # Count good nodes in left and right subtrees.
            res += helper(root.left, max_so_far)
            res += helper(root.right, max_so_far)

            return res        

        return helper(root, root.val)  # Start DFS with the root value as max_so_far.
