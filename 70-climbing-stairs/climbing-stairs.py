class Solution:
    def climbStairs(self, n: int) -> int:
        # Follow-up Questions:
        # 1. What should we return if `n == 0`? (Return 1, as there is one way to "do nothing.")
        # 2. What is the maximum value of `n`? (Assume it fits within reasonable memory constraints.)
        # 3. Are the steps always 1 or 2? (Yes, assume those are the only step sizes.)
        # 4. Can `n` be negative? (No, assume `n >= 0`.)

        # Brute Force Approach:
        # - Use recursion to calculate the number of ways to climb `n` steps:
        #   - At each step, choose to climb 1 or 2 steps.
        #   - Recursively compute the number of ways to climb the remaining steps.
        # - Base Cases:
        #   - `n == 0`: Return 1 (one way to "do nothing").
        #   - `n < 0`: Return 0 (no valid way to climb negative steps).
        # - Time Complexity: O(2^n), as each step creates two recursive calls.
        # - Space Complexity: O(n), due to the recursion stack.

        # Optimized Approach (Dynamic Programming):
        # - Use an array (`res`) to store the number of ways to climb each step:
        #   - `res[i]` represents the number of ways to climb `i` steps.
        #   - Transition Relation: `res[i] = res[i - 1] + res[i - 2]`:
        #     - Ways to climb `i` steps = ways to climb `i-1` steps + ways to climb `i-2` steps.
        # - Initialize `res[0] = 1` and `res[1] = 1` (base cases).
        # - Iterate from 2 to `n` to calculate the result for each step.
        # - Time Complexity: O(n), as we iterate through the array once.
        # - Space Complexity: O(n), to store the array.

        res = [0] * (n + 1)  # Initialize a DP array of size `n + 1`.
        
        # Base cases: There is one way to climb 0 or 1 step.
        res[0] = 1
        res[1] = 1
        
        # Fill the DP array using the transition relation.
        for i in range(2, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        
        return res[n]  # Return the number of ways to climb `n` steps.

# Further Optimization
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 1
#         if n == 1:
#             return 1
        
#         prev2 = 1  # Equivalent to res[0]
#         prev1 = 1  # Equivalent to res[1]
        
#         for i in range(2, n + 1):
#             curr = prev1 + prev2  # res[i] = res[i-1] + res[i-2]
#             prev2 = prev1  # Update prev2
#             prev1 = curr  # Update prev1
        
#         return prev1  # The result for `n`
