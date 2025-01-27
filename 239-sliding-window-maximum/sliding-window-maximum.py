from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Follow-up Questions:
        # 1. What should we return if `nums` is empty? (Return an empty list `[]`.)
        # 2. Can `k` be greater than the length of `nums`? (Assume no, `k <= len(nums)`.)
        # 3. Are all elements in `nums` guaranteed to be integers? (Yes, assume valid input.)
        # 4. Should the solution work for both positive and negative integers? (Yes, handle both cases.)

        # Brute Force Approach:
        # - For each window of size `k`, find the maximum element by iterating through the window.
        # - Slide the window one step to the right and repeat the process.
        # - Time Complexity: O(n * k), where `n` is the length of `nums` and `k` is the window size.
        # - Space Complexity: O(1), as no extra data structures are used.

        # Optimized Approach (Using Deque):
        # - Use a deque to store indices of elements in the current window:
        #   - Maintain elements in the deque in decreasing order.
        #   - Remove indices of elements that fall out of the current window.
        #   - For each element, remove all smaller elements from the deque (as they are irrelevant for the maximum).
        # - Append the maximum of the current window (the first element in the deque) to the result list.
        # - Time Complexity: O(n), as each element is added to and removed from the deque at most once.
        # - Space Complexity: O(k), for the deque, which stores up to `k` elements.

        res = []  # List to store the maximums of each sliding window.
        q = deque()  # Deque to store indices of elements in the current window.
        l = r = 0  # Left and right pointers for the sliding window.

        # Iterate through the array.
        while r < len(nums):
            # Remove indices of elements smaller than the current element.
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove the leftmost element if it's outside the current window.
            if l > q[0]:
                q.popleft()

            # Add the maximum of the current window to the result once the window size reaches `k`.
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1  # Slide the window to the right.

            r += 1  # Move the right pointer.

        return res  # Return the list of maximums.
