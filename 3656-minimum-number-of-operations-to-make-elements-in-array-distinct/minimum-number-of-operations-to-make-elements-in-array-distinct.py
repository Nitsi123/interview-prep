from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Follow-up Questions:
        # 1. What is the maximum size of the array? (Assume it fits in memory.)
        # 2. Are the elements in the array guaranteed to be integers? (Yes.)
        # 3. Can the input array have negative values? (Yes.)
        # 4. What should we return if the array is already distinct? (Return 0 operations.)

        # Brute Force Approach:
        # - Iterate through the array and use a hash set to track unique values.
        # - For each duplicate element encountered, increment the number of operations
        #   needed and update the value to make it unique.
        # - Time Complexity: O(n^2), due to the need to check the uniqueness of updated elements.
        # - Space Complexity: O(n), for storing unique elements in a hash set.

        # Optimized Approach:
        # - Use a hash map to count the occurrences of each element.
        # - Traverse the array from right to left to track duplicates using the hash map.
        # - When a duplicate is found, calculate the minimum number of operations needed
        #   to ensure all elements are unique.
        # - Return the total number of operations required.
        # - Time Complexity: O(n), as we traverse the array and use hash map operations.
        # - Space Complexity: O(n), for the hash map.

        count = {}  # Dictionary to count occurrences of each element.

        # Traverse the array from right to left.
        for i in range(len(nums) - 1, -1, -1):
            # Update the count of the current number.
            count[nums[i]] = count.get(nums[i], 0) + 1
            
            # If the current number appears more than once, calculate the operations needed.
            if count[nums[i]] > 1:
                return (i // 3) + 1  # Return the minimum operations needed.

        return 0  # If no duplicates exist, return 0.
