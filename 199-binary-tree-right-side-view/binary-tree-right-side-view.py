from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Follow-up Questions:
        # 1. What if the tree is empty? (Return `[]`.)
        # 2. Can the tree contain duplicate values? (Yes, assume valid BST or binary tree.)
        # 3. What if the tree is unbalanced? (Still works, as we process each level separately.)
        # 4. Should we return leftmost nodes if no right node exists? (Yes, if the rightmost node is missing.)

        # Brute Force Approach:
        # - Perform a level-order traversal.
        # - Store **all nodes at each level** in an array.
        # - Append **the last node of each level** to the result.
        # - Time Complexity: O(n), since we visit each node once.
        # - Space Complexity: O(n), since we store all nodes at each level.

        # Optimized Approach (BFS with a Queue):
        # - Use a **queue to process nodes level by level** (Breadth-First Search).
        # - Store only the **rightmost node at each level** in `res`.
        # - Time Complexity: O(n), since each node is processed once.
        # - Space Complexity: O(n), worst case for storing nodes in the queue.

        if not root:
            return []

        res = []
        q = deque([root])  # BFS queue initialized with root.

        while q:
            rightSide = None  # Track the last (rightmost) node of each level.
            qLen = len(q)  # Number of nodes in the current level.

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node  # Update last seen node in this level.
                    q.append(node.left)  # Add left child if exists.
                    q.append(node.right)  # Add right child if exists.

            if rightSide:
                res.append(rightSide.val)  # Store the rightmost node.

        return res  # Return list of rightmost nodes.
