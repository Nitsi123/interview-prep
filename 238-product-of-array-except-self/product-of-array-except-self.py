from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Follow-up Questions:
        # 1. Can `nums` contain zero? (Yes, handle cases where one or more zeros exist.)
        # 2. Should we use division? (No, division is not allowed.)
        # 3. Can `nums` contain negative numbers? (Yes, assume all integers are valid.)
        # 4. What should we return if `nums` has only one element? (Not a valid input; assume `len(nums) >= 2`.)

        # Brute Force Approach:
        # - Iterate through `nums` and compute the product of all elements except the current one.
        # - Use nested loops to calculate the product for each index.
        # - Time Complexity: O(n^2), as each element requires iterating over all others.
        # - Space Complexity: O(1), as no extra space is used apart from the result array.

        # Optimized Approach (Prefix and Postfix Multiplication):
        # - Use two passes to compute prefix and postfix products without using division.
        # - **Step 1: Compute prefix product**:
        #   - Initialize `res[i]` with the product of elements before `i`.
        # - **Step 2: Compute postfix product and multiply with prefix**:
        #   - Traverse from the end and update `res[i]` with the accumulated product.
        # - Time Complexity: O(n), since we iterate twice.
        # - Space Complexity: O(1), ignoring the output array.

        res = [1] * len(nums)  # Initialize result array.
        prefix = 1  # Prefix product accumulator.

        # Step 1: Compute prefix products.
        for i in range(len(nums)):
            res[i] = prefix  # Store prefix product in result.
            prefix *= nums[i]  # Update prefix for next iteration.

        postfix = 1  # Postfix product accumulator.

        # Step 2: Compute postfix products and update result.
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # Multiply prefix and postfix.
            postfix *= nums[i]  # Update postfix for next iteration.

        return res  # Return the final product array.
