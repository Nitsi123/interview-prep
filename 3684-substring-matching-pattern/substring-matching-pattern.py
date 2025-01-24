class Solution:
    def hasMatch(self, string: str, pattern: str) -> bool:
        # Follow-up Questions:
        # 1. Is the pattern guaranteed to contain exactly one wildcard `*`? (Assume yes.)
        # 2. Can the input string or pattern be empty? (Assume no; both are non-empty.)
        # 3. Should the match be case-sensitive? (Assume yes, matches are case-sensitive.)
        # 4. Can the `*` be at the beginning or end of the pattern? (Yes, handle these cases properly.)

        # Brute Force Approach:
        # - Generate all possible substrings of the input string that match the left and right parts of the pattern.
        # - Check all possible positions of the wildcard in the string to determine if a match exists.
        # - Time Complexity: O(n^2), where n is the length of the string (checking all substrings).
        # - Space Complexity: O(1), as no additional space is used.

        # Optimized Approach:
        # - Use the `find` method to locate the positions of the left and right parts of the pattern.
        # - Split the pattern into two parts around the wildcard `*`.
        # - Ensure that the left part appears first in the string and the right part follows it.
        # - Time Complexity: O(n), where n is the length of the string (single traversal with `find`).
        # - Space Complexity: O(1), as no additional space is used.

        # Split the pattern into left and right parts around the wildcard `*`.
        left_part, right_part = pattern.split('*')

        # Find the index of the left part in the string.
        left_idx = string.find(left_part)

        # Find the index of the right part in the string, starting after the left part.
        right_idx = string.find(right_part, left_idx + len(left_part))

        # Return True if both parts are found in the correct order; otherwise, return False.
        return left_idx != -1 and right_idx != -1
