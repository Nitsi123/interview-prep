# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Follow-up Questions:
        # 1. What should we return if the input list is empty? (Return None.)
        # 2. Can the `random` pointer point to None? (Yes, assume it can.)
        # 3. Are the node values guaranteed to be integers? (Yes, assume valid input.)
        # 4. Should we preserve the original list? (Yes, the original list should remain unmodified.)

        # Brute Force Approach:
        # - Traverse the list and create copies of each node without linking them.
        # - For each node, traverse the list again to set the `next` and `random` pointers for the copied nodes.
        # - Time Complexity: O(n^2), where `n` is the number of nodes (traversing the list repeatedly).
        # - Space Complexity: O(n), for storing the copied nodes in a hash map.

        # Optimized Approach:
        # - Use a hash map to store the mapping between original nodes and their copies:
        #   - First pass: Create a copy of each node and store it in the hash map.
        #   - Second pass: Use the hash map to set the `next` and `random` pointers for each copied node.
        # - Time Complexity: O(n), as we traverse the list twice.
        # - Space Complexity: O(n), for the hash map.

        curr = head  # Pointer to traverse the original list.
        oldToCopy = {None: None}  # Hash map to store original-to-copy node mapping.

        # Step 1: First pass - Create a copy of each node and store it in the hash map.
        while curr:
            copy = Node(curr.val)  # Create a copy of the current node.
            oldToCopy[curr] = copy  # Map the original node to its copy.
            curr = curr.next  # Move to the next node.

        curr = head  # Reset the pointer to the head of the original list.

        # Step 2: Second pass - Assign the `next` and `random` pointers for the copied nodes.
        while curr:
            copy = oldToCopy[curr]  # Get the copied node from the hash map.
            copy.next = oldToCopy[curr.next]  # Set the `next` pointer for the copy.
            copy.random = oldToCopy[curr.random]  # Set the `random` pointer for the copy.
            curr = curr.next  # Move to the next node.

        # Step 3: Return the head of the copied list.
        return oldToCopy[head]
