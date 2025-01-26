class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Follow-up Questions:
        # 1. What should we return if the string is empty? (Return 0.)
        # 2. Is the input string guaranteed to contain only ASCII characters? (Yes, assume valid input.)
        # 3. Should the solution be case-sensitive? (Yes, 'A' and 'a' are considered different characters.)
        # 4. Can the string contain spaces or special characters? (Yes, handle them as distinct characters.)

        # Optimized Sliding Window Approach:
        # - Use a sliding window to track the current substring without repeating characters.
        # - Maintain a hash map (`used`) to store the last seen index of each character.
        # - Use two pointers, `left` and `right`:
        #   - Move `right` to expand the window and update the hash map for each character.
        #   - If a repeating character is found, adjust `left` to skip the repeating character.
        # - Update the result (`res`) with the length of the current valid substring.
        # - Time Complexity: O(n), where `n` is the length of the string (each character is visited once).
        # - Space Complexity: O(min(n, a)), where `a` is the size of the character set (e.g., 26 for lowercase letters).

        used = {}  # Dictionary to store the last index of each character.
        res = 0  # Initialize the maximum length of the substring.
        left = 0  # Left pointer for the sliding window.

        # Edge Case: If the string is empty, return 0.
        if not s:
            return 0

        # Iterate through the string with the `right` pointer.
        for right, char in enumerate(s):
            # If the character is already in the map and within the current window, update the `left` pointer.
            if char in used and left <= used[char]:
                left = used[char] + 1  # Move `left` to one position after the last occurrence of the character.
            else:
                # Update the maximum length of the substring if no repeat is found in the current window.
                res = max(res, right - left + 1)

            # Update the last seen index of the current character.
            used[char] = right

        return res  # Return the length of the longest substring without repeating characters.
