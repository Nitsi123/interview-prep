# Approach (Breadth-First Search using Queue):
# 1. Initialize an empty list `res` to store each level's values and a queue `q` to manage nodes by level.
# 2. Start by adding the `root` to the queue.
# 3. For each level, calculate the number of nodes (length of `q`).
#    - Initialize an empty list `level` to store values of nodes at this level.
# 4. Loop through each node in the current level:
#    - Dequeue a node, add its value to `level`, and enqueue its left and right children.
# 5. After processing all nodes in a level, add `level` to `res`.
# 6. Continue until all levels are processed and return `res`.

# Time Complexity: O(n), where n is the number of nodes, as each node is processed once.
# Space Complexity: O(n), as we store nodes in the queue and results list.

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # Initialize result list to store each level's values
        q = deque([root] if root else [])  # Initialize queue for BFS traversal
          # Start by adding the root to the queue

        # Perform BFS traversal until there are no nodes left to process
        while q:
            qlen = len(q)  # Number of nodes in the current level
            level = []  # Initialize list to store values at the current level

            # Process each node in the current level
            for i in range(qlen):
                node = q.popleft()  # Dequeue the node from the front of the queue
                
                if node:  # If the node is not None
                    level.append(node.val)  # Add node's value to the current level
                    q.append(node.left)  # Enqueue left child
                    q.append(node.right)  # Enqueue right child
            
            if level:  # After processing, if there are values in the current level
                res.append(level)  # Append the current level's values to the result list
        
        return res  # Return the final list of level order values