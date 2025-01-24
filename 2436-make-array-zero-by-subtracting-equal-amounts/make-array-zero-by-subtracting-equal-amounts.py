from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Follow-up Questions:
        # 1. Can the input list be empty? (Yes, return 0 since no operations are needed.)
        # 2. Are all elements guaranteed to be non-negative? (Yes, as per the problem statement.)
        # 3. What should we return if the input list contains only zeros? (Return 0 since no operations are needed.)
        # 4. Is modifying the input list allowed? (Not necessary for this solution.)

        # Optimized Approach:
        # - The number of unique non-zero elements in the array determines the minimum number of operations.
        # - Each operation reduces all non-zero elements by the smallest non-zero element.
        # - After subtracting the smallest element, it becomes zero, and this process is repeated for the remaining unique non-zero elements.
        # - Time Complexity: O(n), as constructing the set takes O(n) time.
        # - Space Complexity: O(n), for the set of unique elements.

        # Use a set to find unique non-zero elements in the array and return its size.
        return len(set(nums) - {0})
