# Brute Force Approach:
# Check all possible jumps from each index to see if you can reach the last index.
# Time Complexity: O(2^n), where n is the length of `nums`, due to all possible jump combinations.
# Space Complexity: O(n) for recursive call stack.

# Dynamic Programming Approach:
# Use a DP array where each element represents if you can reach the end from that index.
# Time Complexity: O(n^2), as each position checks possible jumps to subsequent positions.
# Space Complexity: O(n) for the DP array.

# Greedy Goal Post Approach:
# Start from the end of the array and use a "goal" pointer to track the last reachable position.
# 1. Initialize `goal` as the last index.
# 2. Iterate from the second last index back to the first:
#    - For each index `i`, check if `i + nums[i]` reaches or exceeds `goal`.
#    - If it does, update `goal` to the current index `i`.
# 3. After the loop, if `goal` is at the start (index 0), return True; otherwise, return False.

# Time Complexity: O(n), as we iterate through `nums` once.
# Space Complexity: O(1), since we only use a few extra variables.

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
