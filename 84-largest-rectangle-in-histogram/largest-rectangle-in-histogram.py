from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Follow-up Questions:
        # 1. Can `heights` be empty? (Yes, return 0.)
        # 2. Can `heights` contain zero? (Yes, zero means no height at that position.)
        # 3. Should we handle negative heights? (No, assume all heights are non-negative.)
        # 4. What if all bars are the same height? (Still works using the stack approach.)

        # Brute Force Approach:
        # - Iterate over all possible left and right bounds.
        # - For each range, find the minimum height and calculate the area.
        # - Time Complexity: O(n^2), checking all ranges.
        # - Space Complexity: O(1), using only a few extra variables.

        # Optimized Approach (Monotonic Increasing Stack):
        # - Maintain a **monotonic increasing stack** to track **histogram bar indices**.
        # - When a **shorter bar is found**, process all taller bars before it.
        # - **Each popped bar determines a maximal rectangle** with height `h` and width `(right-left)`.
        # - Time Complexity: O(n), since each bar is processed once.
        # - Space Complexity: O(n), for the stack.

        maxArea = 0
        stack = []  # Stack stores (index, height).

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:  # If the current bar is shorter than the stack's top
                index, height = stack.pop()  # Pop last stored height.
                maxArea = max(maxArea, height * (i - index))  # Compute area.
                start = index  # Expand left boundary.
            stack.append((start, h))  # Push current bar with updated start.

        # Process remaining bars in stack.
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea  # Return max rectangle area found.
