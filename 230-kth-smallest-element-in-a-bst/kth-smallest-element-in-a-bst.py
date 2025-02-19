# Approach: Iterative In-Order Traversal Using a Stack
# 1. Use an iterative in-order traversal (left-root-right) to find the k-th smallest element in a BST.
# 2. Initialize `n` as a counter to keep track of how many nodes have been visited.
# 3. Traverse to the leftmost node using a `stack`, as this ensures we get the smallest elements first.
# 4. Pop the node from the stack (processing in in-order) and increment `n`.
#    - If `n` equals `k`, return the node's value as the k-th smallest element.
# 5. If not, continue with the right subtree.
# 6. The traversal ends when we reach the k-th smallest element, ensuring efficiency by only visiting nodes as needed.

# Time Complexity: O(h + k), where `h` is the tree height. In a balanced BST, h = O(log n).
#   - We traverse down to the leftmost node initially and then visit `k` nodes in order.
# Space Complexity: O(h), where `h` is the height of the tree.
#   - This is the maximum space used by the stack for the recursion depth.

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0  # Initialize counter to track the number of nodes processed
        stack = []  # Stack for iterative in-order traversal
        cur = root  # Start traversal from the root node

        # Perform in-order traversal until we find the k-th smallest element
        while cur or stack:
            # Traverse left subtree to reach the smallest elements first
            while cur:
                stack.append(cur)  # Add current node to stack
                cur = cur.left  # Move to the left child
            
            # Process the current node
            cur = stack.pop()  # Retrieve node from the top of the stack
            n += 1  # Increment the count of processed nodes

            # If we have reached the k-th smallest element, return its value
            if n == k:
                return cur.val  # Return the k-th smallest element
            
            # Move to the right subtree to continue in-order traversal
            cur = cur.right