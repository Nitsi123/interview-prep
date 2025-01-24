from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Follow-up Questions:
        # 1. Can the input list be empty? (Yes, return 0 as no transactions are possible.)
        # 2. Can the input list have only one element? (Yes, return 0 as no transactions can occur.)
        # 3. Can we buy and sell multiple times? (Yes, we can buy and sell multiple times to maximize profit.)
        # 4. Are negative prices possible? (No, prices are guaranteed to be non-negative.)

        # Brute Force Approach:
        # - Use a nested loop to simulate all possible pairs of buy and sell days.
        # - Track and sum the profit for all valid transactions where the selling price is greater than the buying price.
        # - Time Complexity: O(n^2), as every possible pair is evaluated.
        # - Space Complexity: O(1), as no extra data structures are used.

        # Optimized Approach:
        # - Traverse the array and add up the profit for every increasing price pair.
        # - If `prices[i] > prices[i-1]`, the difference is added to the total profit.
        # - This approach greedily accumulates profit for every upward price movement.
        # - Time Complexity: O(n), as the list is traversed once.
        # - Space Complexity: O(1), as no extra space is used.

        total = 0  # Initialize total profit to 0

        # Traverse the price array, starting from the second day
        for i in range(1, len(prices)):
            # If there is a profit opportunity (price increased from the previous day):
            if prices[i] - prices[i - 1] > 0:
                total += prices[i] - prices[i - 1]  # Add the profit to the total

        return total  # Return the total accumulated profit
