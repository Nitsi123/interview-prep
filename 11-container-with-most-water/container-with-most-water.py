from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Follow-up Questions:
        # 1. Can `height` contain negative values? (No, assume all heights are non-negative.)
        # 2. Can `height` contain duplicate values? (Yes, the solution should handle this.)
        # 3. Should we return the maximum area or the indices? (Return the maximum area.)
        # 4. What if `height` has less than two elements? (Invalid input; assume `len(height) >= 2`.)

        # Brute Force Approach:
        # - Consider every pair of lines `(i, j)`, compute the area.
        # - Formula: `min(height[i], height[j]) * (j - i)`.
        # - Track the maximum area found.
        # - Time Complexity: O(n^2), due to nested loops checking all pairs.
        # - Space Complexity: O(1), as only a few extra variables are used.

        # Optimized Approach (Two-Pointer Technique):
        # - Use two pointers, `l` at the beginning and `r` at the end.
        # - Compute the area at each step.
        # - **Key Insight**: The maximum area is limited by the shorter height.
        # - Move the pointer at the **shorter height** inward to try maximizing area.
        # - **Why?**
        #   - Moving the taller height does not help because the height constraint remains.
        #   - Moving the shorter height allows for a potential increase in area.
        # - Time Complexity: O(n), as we traverse the array once.
        # - Space Complexity: O(1), as only pointers and a max variable are used.

        l, r = 0, len(height) - 1  # Initialize two pointers.
        max_area = 0  # Store the maximum area found.

        while l < r:
            area = min(height[l], height[r]) * (r - l)  # Calculate current area.
            max_area = max(max_area, area)  # Update maximum area.

            # Move the pointer at the smaller height.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area  # Return the maximum water area found.
