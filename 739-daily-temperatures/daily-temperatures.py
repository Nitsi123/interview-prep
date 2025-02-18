from typing import List

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # Follow-up Questions:
        # 1. Can temperatures be negative? (Yes, assume any integer values.)
        # 2. Can `temps` contain duplicates? (Yes, and they are handled correctly.)
        # 3. What if `temps` is empty? (Return `[]`.)
        # 4. What should we return if no future temperature is warmer? (Return `0` for that day.)

        # Brute Force Approach:
        # - For each day `i`, check all future days `j > i` for a higher temperature.
        # - Store `j - i` in the result when a warmer temperature is found.
        # - Time Complexity: O(n^2), as each day scans all future days.
        # - Space Complexity: O(1), storing only result.

        # Optimized Approach (Monotonic Stack):
        # - Use a **decreasing monotonic stack**:
        #   - Stores pairs `(temperature, index)`.
        #   - As soon as a warmer temperature is found, update results and pop stack.
        # - Ensures each element is processed **only once**.
        # - Time Complexity: O(n), since each element is pushed/popped once.
        # - Space Complexity: O(n), for the stack.

        res = [0] * len(temps)  # Initialize result array with zeros.
        stack = []  # Monotonic decreasing stack (stores `(temperature, index)`).

        for i, t in enumerate(temps):
            # Ensure the stack maintains decreasing order.
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx  # Compute waiting days.
            stack.append((t, i))  # Store current temperature and index.

        return res  # Return final waiting days array.
