from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Follow-up Questions:
        # 1. What should we return if `nums` is empty? (Return 0.)
        # 2. Can `nums` contain negative numbers? (Yes, assume all integers are allowed.)
        # 3. Are duplicate numbers possible? (Yes, but they do not affect the result.)
        # 4. What is the expected time complexity? (Better than O(n log n), ideally O(n).)

        # Brute Force Approach:
        # - Sort `nums` and scan for consecutive sequences.
        # - Iterate through the sorted list, counting the longest contiguous sequence.
        # - Time Complexity: O(n log n), due to sorting.
        # - Space Complexity: O(1), if sorting is done in-place.

        # Optimized Approach (Using HashSet):
        # - Convert `nums` into a set for O(1) lookups.
        # - Iterate through each number:
        #   - Only start counting if `num - 1` is not in the set (ensures sequence starts here).
        #   - Use a `while` loop to count consecutive numbers.
        # - This ensures each number is visited once, making it O(n).
        # - Time Complexity: O(n), as each number is processed once.
        # - Space Complexity: O(n), for storing numbers in a set.

        numSet = set(nums)  # Convert list to set for O(1) lookups.
        res = 0  # Stores the length of the longest consecutive sequence.

        for num in numSet:  # Iterate through the set instead of the original list.
            if (num - 1) not in numSet:  # Only process numbers that are sequence starters.
                length = 1  # Initialize sequence length.
                while num + length in numSet:  # Expand the sequence.
                    length += 1
                res = max(res, length)  # Update result with the longest found.

        return res  # Return the longest consecutive sequence length.
