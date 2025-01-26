from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Follow-up Questions:
        # 1. What is the maximum value of `n`? (Assume it fits in memory.)
        # 2. Are the parentheses guaranteed to be balanced? (Yes, the task is to generate only valid combinations.)
        # 3. Can `n` be 0? (Yes, return an empty list as there are no valid combinations.)

        # Brute Force Approach:
        # - Generate all possible strings of length 2 * n containing '(' and ')'.
        # - Check each string to see if it is valid (balanced).
        # - Add valid strings to the result.
        # - Time Complexity: O(2^(2n) * n), as there are 2^(2n) combinations, and each is validated in O(n).
        # - Space Complexity: O(n) for the recursion stack and the intermediate strings.

        # Optimized Approach:
        # - Use backtracking to generate valid combinations directly:
        #   - Maintain counts of open and close parentheses.
        #   - Add '(' if the number of open parentheses is less than `n`.
        #   - Add ')' if the number of close parentheses is less than the number of open parentheses.
        #   - When the length of the current string is 2 * n, add it to the result.
        # - Time Complexity: O(4^n / sqrt(n)), which is the number of valid combinations.
        # - Space Complexity: O(n) for the recursion stack.

        path = []  # Temporary list to store the current combination of parentheses.
        res = []   # List to store all valid combinations.

        def dfs(open_count, close_count):
            # Base case: If the current combination has 2 * n characters, add it to the result.
            if len(path) == 2 * n:
                res.append("".join(path))  # Convert the path to a string and store it.
                return
            
            # Add an open parenthesis if the count is less than `n`.
            if open_count < n:
                path.append('(')           # Add '(' to the current combination.
                dfs(open_count + 1, close_count)  # Recur with incremented open count.
                path.pop()                 # Backtrack by removing the last added '('.

            # Add a close parenthesis if the count is less than the open count.
            if close_count < open_count:
                path.append(')')           # Add ')' to the current combination.
                dfs(open_count, close_count + 1)  # Recur with incremented close count.
                path.pop()                 # Backtrack by removing the last added ')'.

        # Start the recursive backtracking with 0 open and close parentheses.
        dfs(0, 0)
        return res  # Return all valid combinations of parentheses.
