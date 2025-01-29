from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Follow-up Questions:
        # 1. Can the tree contain negative values? (Yes, the path sum may be negative.)
        # 2. Can the tree be empty? (No, assume at least one node is present.)
        # 3. Can the maximum path go through the root? (Not necessarily; any node can be the highest sum root.)
        # 4. Should the path be continuous? (Yes, the path must be connected through parent-child nodes.)

        # Brute Force Approach:
        # - Compute the sum for every possible path in the tree.
        # - Recursively traverse all possible paths and track the maximum.
        # - This results in redundant calculations.
        # - Time Complexity: O(n^2), due to repeated path calculations.
        # - Space Complexity: O(n), for recursion stack in an unbalanced tree.

        # Optimized Approach (DFS with Backtracking):
        # - Use Depth-First Search (DFS) to calculate the maximum path sum for each subtree.
        # - Track the global max path sum (`res`).
        # - At each node:
        #   - Compute max sum from left and right children.
        #   - Ignore negative sums (use max(left, 0) and max(right, 0)).
        #   - Compute possible max path sum: left + right + node value.
        #   - Update `res` with the highest path sum found.
        #   - Return **only the max sum of one branch** (`max(left, right) + node.val`) to ensure a valid path.
        # - Time Complexity: O(n), as each node is visited once.
        # - Space Complexity: O(n), for recursion stack in an unbalanced tree.

        res = [root.val]  # Track the maximum path sum.

        def dfs(root):
            if root is None:
                return 0
            
            # Recursively calculate max path sum for left and right subtrees.
            lMax = dfs(root.left)
            rMax = dfs(root.right)

            # Ignore negative contributions to ensure we maximize sum.
            lMax = max(lMax, 0)
            rMax = max(rMax, 0)

            # Compute the best path sum **including both left and right**.
            res[0] = max(res[0], lMax + rMax + root.val)

            # Return the max sum of one side + node value (ensuring valid path structure).
            return max(lMax, rMax) + root.val
        
        dfs(root)
        return res[0]  # Return the global max path sum.
