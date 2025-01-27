from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Follow-up Questions:
        # 1. Can the input array contain negative numbers? (Yes, handle negative numbers properly.)
        # 2. Can the target sum `k` be negative? (Yes, handle it properly.)
        # 3. What should we return if there are no subarrays with the sum equal to `k`? (Return 0.)
        # 4. Are all numbers integers? (Yes, assume valid input.)

        # Brute Force Approach:
        # - Iterate through all subarrays of the input array:
        #   - For each subarray, calculate its sum.
        #   - If the sum matches `k`, increment the result counter.
        # - Time Complexity: O(n^2), where `n` is the length of the array (O(n^2) for generating subarrays).
        # - Space Complexity: O(1), as no extra space is used.

        # Optimized Approach:
        # - Use a prefix sum and a hash map (`prefixMap`) to track the count of prefix sums:
        #   - Calculate the current prefix sum (`currSum`) as you iterate through the array.
        #   - For each prefix sum, calculate the difference (`currSum - k`).
        #     - If this difference exists in the hash map, it means a subarray with the sum `k` ends at the current index.
        #   - Update the result counter with the count of such subarrays.
        #   - Update the hash map with the current prefix sum.
        # - Time Complexity: O(n), as we traverse the array once.
        # - Space Complexity: O(n), for the hash map storing prefix sums.

        res = 0  # Initialize the result counter.

        prefixMap = {0: 1}  # Hash map to store prefix sums and their counts.
        currSum = 0  # Initialize the current prefix sum.

        # Iterate through the array.
        for n in nums:
            currSum += n  # Update the current prefix sum.
            diff = currSum - k  # Calculate the difference needed to form a subarray sum equal to `k`.
            
            # Check if the difference exists in the hash map.
            res += prefixMap.get(diff, 0)  # Add the count of such subarrays to the result.

            # Update the hash map with the current prefix sum.
            prefixMap[currSum] = 1 + prefixMap.get(currSum, 0)
        
        return res  # Return the total count of subarrays with the sum equal to `k`.
