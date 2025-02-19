# Approach: Recursive DFS with Range Validation
# 1. Use a recursive helper function `valid` to traverse the tree and check
#    if each node’s value falls within a specified range.
# 2. Start from the root, with the range set to `(-inf, inf)`:
#    - For each node, ensure its value is greater than the left boundary
#      and less than the right boundary.
#    - Recursively call `valid` on the left child, updating the right boundary
#      to the current node's value.
#    - Recursively call `valid` on the right child, updating the left boundary
#      to the current node's value.
# 3. If all nodes meet the criteria, the tree is a valid Binary Search Tree (BST).

# Time Complexity: O(n), where `n` is the number of nodes in the tree, as we visit each node once.
# Space Complexity: O(h), where `h` is the height of the tree, due to the recursion stack.
#   - For a balanced tree, this is O(log n); for a skewed tree, it could be O(n).

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to validate the BST by checking value boundaries
        def valid(node, left, right):
            if not node:  # Base case: an empty node is valid
                return True

            # If node's value violates the BST property, return False
            if not(left < node.val < right):
                return False
            
            # Recursively validate the left subtree
            # Left subtree nodes must be < current node's value
            return (valid(node.left, left, node.val) and
                    # Recursively validate the right subtree
                    # Right subtree nodes must be > current node's value
                    valid(node.right, node.val, right))
        
        # Start the validation from the root with initial range (-inf, inf)
        return valid(root, float("-inf"), float("inf"))