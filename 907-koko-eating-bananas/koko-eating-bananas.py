from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Follow-up Questions:
        # 1. What should we return if `piles` is empty? (Assume valid input, always at least one pile.)
        # 2. Can `h` be smaller than the number of piles? (No, `h >= len(piles)` is guaranteed.)
        # 3. Should the result be an integer? (Yes, eating speed `k` must be an integer.)
        # 4. What is the maximum value in `piles`? (Assume `max(piles)` is reasonable for computation.)

        # Brute Force Approach:
        # - Try all possible eating speeds from 1 to `max(piles)`.
        # - For each speed `k`, simulate eating to check if `h` hours are sufficient.
        # - Return the smallest `k` that allows all bananas to be eaten within `h` hours.
        # - Time Complexity: O(max(piles) * n), where `n` is the number of piles.
        # - Space Complexity: O(1), as no extra data structures are used.

        # Optimized Approach (Binary Search on k):
        # - The minimum possible eating speed is `1` (slowest).
        # - The maximum possible eating speed is `max(piles)` (eating the largest pile in one hour).
        # - Use binary search between `[1, max(piles)]` to find the smallest `k` that satisfies the condition.
        # - Time Complexity: O(n log max(piles)), as binary search reduces the range logarithmically.
        # - Space Complexity: O(1), as only variables are used.

        l = 1  # Left boundary (slowest eating speed).
        r = max(piles)  # Right boundary (fastest possible eating speed).
        res = r  # Initialize result to the max speed.

        while l <= r:
            k = (l + r) // 2  # Midpoint as the potential eating speed.
            hours = 0  # Track total hours needed.

            # Calculate the total hours needed to eat all piles at speed `k`.
            for p in piles:
                hours += math.ceil(p / k)  # Ceiling ensures partial piles take full hours.

            # If Koko can eat all bananas within `h` hours, try a smaller speed.
            if hours <= h:
                res = min(res, k)  # Update the minimum valid speed.
                r = k - 1  # Try a slower eating speed.
            else:
                l = k + 1  # Increase the eating speed.

        return res  # Return the minimum required eating speed.
