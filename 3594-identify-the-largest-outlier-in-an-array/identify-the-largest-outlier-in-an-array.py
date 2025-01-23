from typing import List
from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # Follow-up Questions:
        # 1. Can the input array contain duplicate numbers? (Assume yes.)
        # 2. Are all numbers in the input guaranteed to be integers? (Assume yes.)
        # 3. Should we return -∞ if no valid outlier exists? (Assume yes.)
        # 4. Is the input array always non-empty? (Assume yes.)

        # Brute Force Approach:
        # - Iterate through each element in the array.
        # - Temporarily remove it, and calculate the sum of the remaining numbers.
        # - Check if the remaining sum is even and if it is divisible by 2 with one number in the array
        #   being half of this sum.
        # - If the condition is satisfied, keep track of the largest outlier found so far.
        # - Time Complexity: O(n^2), as we iterate through every pair of numbers.
        # - Space Complexity: O(1), as no extra data structures are used.

        # Optimized Approach:
        # - Precompute the total sum of the array.
        # - Use a Counter to keep track of the frequency of each number.
        # - Iterate through the array:
        #   - Subtract the current number from the total sum.
        #   - Check if the remaining sum is even and divisible by 2 with the corresponding complement
        #     present in the Counter.
        #   - If the condition is satisfied, update the largest outlier.
        #   - Restore the total sum and frequency after the iteration.
        # - Time Complexity: O(n), as we traverse the array once and use a hash map (Counter) for lookups.
        # - Space Complexity: O(n), due to the Counter used to store frequencies.

        # Calculate the total sum of the array.
        total_sum = sum(nums)
        # Use a Counter to store the frequency of each number in the array.
        counts = Counter(nums)

        # Initialize the largest outlier to negative infinity.
        outlier = -float("inf")

        # Iterate through each number in the array.
        for num in nums:
            total_sum -= num  # Temporarily remove the current number from the sum.
            counts[num] -= 1  # Reduce the frequency of the current number.

            # Check if the remaining sum is even and if its half exists in the array.
            if total_sum % 2 == 0 and counts[total_sum // 2] > 0:
                outlier = max(outlier, num)  # Update the largest outlier.

            total_sum += num  # Restore the total sum.
            counts[num] += 1  # Restore the frequency of the current number.

        return outlier  # Return the largest outlier found.
