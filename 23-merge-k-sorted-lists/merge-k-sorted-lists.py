from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Follow-up Questions:
        # 1. What should we return if the input list of lists is empty? (Return `None`.)
        # 2. Are the input linked lists guaranteed to be sorted? (Yes, assume they are sorted.)
        # 3. Can there be duplicate values across different lists? (Yes, handle duplicates properly.)
        # 4. What is the maximum value of `k` (number of linked lists)? (Assume it fits in memory.)

        # Optimized Approach:
        # - Use a divide-and-conquer strategy to iteratively merge pairs of linked lists.
        # - Repeatedly merge two lists at a time until only one list remains:
        #   - Use a helper function (`merge`) to merge two sorted linked lists.
        # - Time Complexity: O(N log k), where `N` is the total number of nodes across all lists, and `k` is the number of linked lists.
        # - Space Complexity: O(1) for merging, and O(log k) for the recursion stack in the divide-and-conquer process.

        # Edge case: If the input list is empty, return None.
        if not lists or len(lists) == 0:
            return None

        # Continue merging lists until only one list remains.
        while len(lists) > 1:
            mergedList = []  # Temporary list to store merged results.

            # Merge lists in pairs.
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # First list in the pair.
                l2 = lists[i + 1] if (i + 1) < len(lists) else None  # Second list in the pair, if it exists.
                mergedList.append(self.merge(l1, l2))  # Merge the two lists and append the result.

            # Replace the original list with the merged results.
            lists = mergedList

        # Return the fully merged linked list.
        return lists[0]

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to merge two sorted linked lists.
        
        # Create a dummy node to simplify the merging process.
        head = ListNode()
        temp = head

        # Merge the lists by comparing the nodes from both lists.
        while l1 and l2:
            if l1.val < l2.val:  # If the value in l1 is smaller, add it to the merged list.
                temp.next = l1
                l1 = l1.next
            else:  # Otherwise, add the value from l2.
                temp.next = l2
                l2 = l2.next
            temp = temp.next  # Move to the next node in the merged list.

        # Add any remaining nodes from l1 or l2.
        while l1:
            temp.next = l1
            l1 = l1.next
            temp = temp.next

        while l2:
            temp.next = l2
            l2 = l2.next
            temp = temp.next

        # Return the merged list, starting from the first actual node.
        return head.next
