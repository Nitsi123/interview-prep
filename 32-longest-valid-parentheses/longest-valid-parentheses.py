from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Follow-up Questions:
        # 1. What should we return if `s` is empty? (Return 0.)
        # 2. Can `s` contain characters other than `(` and `)`? (No, assume valid input.)
        # 3. Are nested parentheses handled correctly? (Yes, this approach counts valid sequences.)
        # 4. Should we return the substring or just the length? (Return only the length.)

        # Brute Force Approach:
        # - Generate all possible substrings and check if they are valid.
        # - Use a helper function to check validity by counting open and close brackets.
        # - Time Complexity: O(n^3), as we generate all substrings and validate them.
        # - Space Complexity: O(1), as only counters are used.

        # Optimized Approach (Two-pass Left-Right & Right-Left Scan):
        # - **First pass (left to right)**:
        #   - Count `(` and `)`, updating `maxLen` when counts are equal.
        #   - Reset counts if `)` exceeds `(` (invalid prefix).
        # - **Second pass (right to left)**:
        #   - Count `(` and `)`, updating `maxLen` when counts are equal.
        #   - Reset counts if `(` exceeds `)` (invalid suffix).
        # - Ensures all valid substrings are counted, even when an excess of `)` or `(` exists.
        # - Time Complexity: O(n), as we scan the string twice.
        # - Space Complexity: O(1), using only counters.

        l_count = r_count = maxLen = 0

        # Left-to-right scan.
        for i in range(len(s)):
            if s[i] == '(':
                l_count += 1
            else:
                r_count += 1
            
            if l_count == r_count:
                maxLen = max(maxLen, l_count + r_count)
            elif r_count > l_count:
                l_count = r_count = 0  # Reset when too many closing brackets.

        # Reset counters for right-to-left scan.
        l_count = r_count = 0

        # Right-to-left scan.
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                l_count += 1
            else:
                r_count += 1
            
            if l_count == r_count:
                maxLen = max(maxLen, l_count + r_count)
            elif l_count > r_count:
                l_count = r_count = 0  # Reset when too many opening brackets.

        return maxLen  # Return the longest valid parentheses length.
