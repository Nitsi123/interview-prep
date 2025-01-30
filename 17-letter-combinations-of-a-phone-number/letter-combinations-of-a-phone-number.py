from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Follow-up Questions:
        # 1. What should we return if `digits` is empty? (Return an empty list `[]`.)
        # 2. Are the digits guaranteed to be between `2-9`? (Yes, assume valid input.)
        # 3. Do we need to return the combinations in lexicographical order? (Yes, naturally achieved via recursion.)
        # 4. How do we handle large input sizes? (Use backtracking to efficiently generate combinations.)

        # Brute Force Approach:
        # - Generate all possible combinations of letters for each digit.
        # - Use nested loops to iterate through all possibilities.
        # - This results in exponential growth in complexity.
        # - Time Complexity: O(3^n * 4^m), where `n` is the number of digits mapped to 3 letters and `m` is the number mapped to 4.
        # - Space Complexity: O(3^n * 4^m), to store the result set.

        # Optimized Approach (Backtracking with DFS):
        # - Use a recursive function to generate all possible letter combinations.
        # - Append valid combinations to `res` when the length matches `digits`.
        # - Use backtracking to explore all options efficiently.
        # - Time Complexity: O(3^n * 4^m), as each digit generates multiple branches.
        # - Space Complexity: O(n), for recursion depth (maximum depth is the length of `digits`).

        dialpad = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        if not digits:  # Edge case: empty input.
            return []
        
        res = []  # Stores all valid letter combinations.

        def dfs(path, i):
            # Base case: if path length equals input length, store result.
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            # Get letters corresponding to the current digit.
            for char in dialpad[digits[i]]:
                path.append(char)  # Add character.
                dfs(path, i + 1)  # Recursive call for next digit.
                path.pop()  # Backtrack to try a new letter.

        dfs([], 0)  # Start DFS from index 0.
        return res  # Return all generated combinations.
