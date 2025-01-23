from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Follow-up Questions:
        # 1. Can the input array contain negative numbers or duplicates? (Assume yes.)
        # 2. What should be returned if no solution exists? (Assume a solution always exists.)
        # 3. Should indices be returned in any specific order? (Return them in the order found.)

        # Brute Force Approach:
        # - Iterate through each number in the array.
        # - For each number, iterate through every other number to check if their sum equals the target.
        # - Return the indices of the first pair of numbers that sum up to the target.
        # - Time Complexity: O(n^2) because of nested loops to check every pair.
        # - Space Complexity: O(1) as no additional data structures are used.

        # Optimized Approach:
        # - Use a hash map to store each number and its index as you iterate through the array.
        # - For each number, calculate the complement (target - current number).
        # - Check if the complement exists in the hash map:
        #     - If yes, return the indices of the complement and the current number.
        #     - Otherwise, add the current number and its index to the hash map.
        # - Time Complexity: O(n) because we traverse the list once.
        # - Space Complexity: O(n) because the hash map stores up to n elements.

        hashmap = {}  # Initialize an empty hash map to store number:index pairs.

        for i, num in enumerate(nums):  # Traverse the list with both index and value.
            complement = target - num  # Calculate the complement needed to reach the target.

            # Check if the complement is already in the hash map.
            if complement in hashmap:
                return [hashmap[complement], i]  # Return indices of the complement and current number.

            # If the complement is not found, add the current number and its index to the hash map.
            hashmap[num] = i
