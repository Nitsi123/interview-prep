class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Follow-up Questions:
        # 1. Can `x` or `n` be negative? (Yes, handle both cases properly.)
        # 2. What should we return if `x == 0` and `n > 0`? (Return 0.)
        # 3. What should we return if `n == 0`? (Return 1, as any number to the power of 0 is 1.)
        # 4. Are there constraints on the range of `n`? (Assume it fits within 32-bit integers.)

        # Brute Force Approach:
        # - Multiply `x` by itself `n` times for positive `n`.
        # - For negative `n`, calculate `1 / (x^|n|)` by dividing 1 by the result of positive power.
        # - Time Complexity: O(n), as it involves `n` multiplications.
        # - Space Complexity: O(1), as no extra space is used.

        # Optimized Approach (Recursive):
        # - Use the concept of divide-and-conquer:
        #   - Split the power calculation into smaller subproblems by halving `n` recursively.
        #   - Use the relation \(x^n = (x^{n/2})^2\) to compute results faster.
        #   - If `n` is odd, account for the extra multiplication by \(x\).
        # - Base Cases:
        #   - If `x == 0`, return 0 (any power of 0 is 0).
        #   - If `n == 0`, return 1 (any number to the power of 0 is 1).
        # - Time Complexity: O(log n), as `n` is halved in each recursive step.
        # - Space Complexity: O(log n), due to the recursion stack.

        def helper(x, n):
            # Base case: If the base is 0, return 0 (special case for 0^n).
            if x == 0:
                return 0

            # Base case: If the exponent is 0, return 1.
            if n == 0:
                return 1

            # Recursively calculate the result for half the exponent.
            res = helper(x, n // 2)
            res = res * res  # Square the result for half the exponent.

            # If `n` is odd, multiply by `x` to account for the remaining factor.
            return res * x if n % 2 != 0 else res

        # Handle the case where `n` is negative.
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res  # If `n` is negative, return the reciprocal of the result.
