# Brute Force Approach:
# Iterate over each possible pair of elements in the list.
# For each pair, check if their sum equals the target.
# If a pair that sums to the target is found, return their indices (1-based).
# Time Complexity: O(n^2), where n is the length of the list, as we check each pair of elements.
# Space Complexity: O(1), since we only use a few variables for indices.

# Optimized Approach:
# Use a two-pointer technique to find two numbers that add up to the target.
# - Initialize two pointers: `l` at the start (left) and `r` at the end (right) of the sorted list.
# - Calculate the current sum of the elements at the `l` and `r` pointers.
#   - If the sum is greater than the target, move the right pointer `r` one step left to decrease the sum.
#   - If the sum is less than the target, move the left pointer `l` one step right to increase the sum.
#   - If the sum equals the target, return the 1-based indices of `l` and `r`.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Initialize two pointers

        while l < r:  # Continue until the two pointers meet
            currSum = numbers[l] + numbers[r]  # Calculate the current sum

            if currSum > target:  # If the sum is too large
                r -= 1  # Move the right pointer left to decrease the sum
            elif currSum < target:  # If the sum is too small
                l += 1  # Move the left pointer right to increase the sum
            else:  # If the sum equals the target
                return [l + 1, r + 1]  # Return 1-based indices

# Time Complexity: O(n), where n is the length of the numbers list, as we scan the list once with two pointers.
# Space Complexity: O(1), as we only use a few variables for pointers and the current sum.