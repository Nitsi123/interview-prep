from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Follow-up Questions:
        # 1. Can candidates contain duplicate numbers? (Yes, must handle duplicates.)
        # 2. Should combinations be unique? (Yes, no duplicate sets in `res`.)
        # 3. Should candidates be used multiple times? (No, each number is used once.)
        # 4. Can candidates contain negative numbers? (No, assume all are positive.)

        # Brute Force Approach:
        # - Generate all subsets of `candidates`.
        # - Check if any subset sums to `target` and store unique ones.
        # - Requires tracking and removing duplicates manually.
        # - Time Complexity: O(2^n) (subsets generation) + O(n log n) (sorting).
        # - Space Complexity: O(n), due to recursion depth.

        # Optimized Approach (Backtracking with Sorting & Skip Duplicates):
        # - **Sort `candidates`** to make it easier to skip duplicates.
        # - **Backtrack through the list, choosing or skipping elements**.
        # - **Skip duplicate elements** at the same depth to avoid duplicate combinations.
        # - Time Complexity: O(2^n), since we explore subsets.
        # - Space Complexity: O(n), for the recursion depth.

        res = []
        candidates.sort()  # Sorting helps handle duplicates.

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())  # Valid combination found.
                return
            if total > target or i == len(candidates):  # Base case: exceed target.
                return
            
            # Choose the current candidate.
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            # Skip duplicate candidates at the same level.
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)  # Start DFS.
        return res  # Return unique combinations.
