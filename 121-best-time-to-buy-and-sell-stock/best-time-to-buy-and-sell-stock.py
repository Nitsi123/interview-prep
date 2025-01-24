from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Follow-up Questions:
        # 1. What should we return if the prices list is empty? (Return 0, as no transaction is possible.)
        # 2. Can the prices list have only one element? (Yes, return 0 since no transaction can occur.)
        # 3. Can we buy and sell on the same day? (No, buying and selling must occur on different days.)
        # 4. Are negative prices possible? (Assume no, as prices are non-negative.)

        # Brute Force Approach:
        # - Use a nested loop to calculate the profit for every pair of days (i, j) where i < j.
        # - Keep track of the maximum profit seen so far.
        # - Time Complexity: O(n^2), as we evaluate all possible pairs of days.
        # - Space Complexity: O(1), as no extra data structures are used.

        # Optimized Approach:
        # - Use a two-pointer technique to track the minimum price (buy day) and maximum profit.
        # - Initialize two pointers, `l` (buy day) and `r` (sell day), at the start and move `r` forward:
        #   - If the price at `l` is greater than the price at `r`, move `l` to `r`.
        #   - Calculate the profit as `prices[r] - prices[l]`, and update the maximum profit.
        # - Time Complexity: O(n), as we traverse the list once.
        # - Space Complexity: O(1), as no extra data structures are used.

        l = 0  # Pointer to the buy day
        r = 1  # Pointer to the sell day
        res = 0  # Initialize the maximum profit to 0

        # Traverse the prices array with the two pointers
        while r < len(prices):
            # Calculate the profit for the current buy and sell days
            res = max(res, prices[r] - prices[l])
            
            # If the price at the buy day (`l`) is greater than the price at the sell day (`r`),
            # move the buy day pointer to the sell day pointer
            if prices[l] > prices[r]:
                l = r
            
            # Move the sell day pointer to the next day
            r += 1

        return res  # Return the maximum profit found
