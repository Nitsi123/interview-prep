from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Follow-up Questions:
        # 1. What should we return if the input list is empty? (Return 0.)
        # 2. Can the input have negative heights? (Assume no, heights are non-negative.)
        # 3. What is the maximum size of the height list? (Assume it fits in memory.)
        # 4. Are all heights integers? (Yes, as per the problem statement.)

        # Brute Force Approach:
        # - For each bar, calculate the amount of water it can trap by finding the maximum height
        #   to its left and right.
        # - Water trapped at a bar = min(max_left, max_right) - height of the bar.
        # - Sum up water trapped for all bars.
        # - Time Complexity: O(n^2) because for each bar, we compute max_left and max_right.
        # - Space Complexity: O(1) as no extra space is used.

        # Optimized Approach:
        # - Use two pointers (left and right) to traverse the array.
        # - Maintain `lMax` (maximum height from the left) and `rMax` (maximum height from the right).
        # - Calculate water trapped at each bar while moving the pointers toward each other.
        # - If `lMax < rMax`, move the left pointer and calculate water based on `lMax`.
        # - If `rMax <= lMax`, move the right pointer and calculate water based on `rMax`.
        # - Time Complexity: O(n) because we traverse the array once.
        # - Space Complexity: O(1) as no extra space is used beyond variables.

        if len(height) == 0:  # Edge case: If the height array is empty, no water can be trapped.
            return 0

        # Initialize two pointers at the beginning and end of the array.
        l = 0
        r = len(height) - 1
        # Variables to keep track of the maximum heights seen so far from the left and right.
        lMax = height[l]
        rMax = height[r]
        # Variable to accumulate the total amount of trapped water.
        res = 0

        # Traverse the height array using the two pointers.
        while l < r:
            if lMax < rMax:
                # If the left maximum is less than the right maximum:
                l += 1  # Move the left pointer to the right.
                lMax = max(lMax, height[l])  # Update the left maximum.
                res += lMax - height[l]  # Add the water trapped at the current bar.
            else:
                # If the right maximum is less than or equal to the left maximum:
                r -= 1  # Move the right pointer to the left.
                rMax = max(rMax, height[r])  # Update the right maximum.
                res += rMax - height[r]  # Add the water trapped at the current bar.

        return res  # Return the total amount of trapped water.
