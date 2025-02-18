from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Follow-up Questions:
        # 1. Can `s` contain lowercase characters? (No, assume all uppercase letters.)
        # 2. Can `k` be greater than `len(s)`? (No, assume `0 <= k <= len(s)`)
        # 3. Should the result include `k` replacements or just valid substrings? (Include up to `k` replacements.)
        # 4. What if `k == 0`? (Find the longest substring with repeating characters.)

        # Brute Force Approach:
        # - Try all substrings of `s` and check if they can be converted to all the same character.
        # - Use a frequency map to count character occurrences.
        # - Time Complexity: O(n^2), iterating through all substrings.
        # - Space Complexity: O(1), storing only a frequency count.

        # Optimized Approach (Sliding Window with Frequency Count):
        # - Maintain a sliding window `[l, r]` where we replace at most `k` characters.
        # - Track `maxf`: the highest frequency of any character in the window.
        # - The **window size minus `maxf`** gives the number of replacements needed.
        # - If `(r - l + 1) - maxf > k`, the window is invalid → shrink `l` (move left).
        # - Update `res` with the max valid window length.
        # - Time Complexity: O(n), since `l` and `r` each move at most `n` times.
        # - Space Complexity: O(1), since we only store character frequencies.

        l = 0  # Left pointer of the window.
        res = 0  # Stores the longest valid window length.
        count = {}  # Character frequency map.
        maxf = 0  # Tracks the max frequency of any single character in the window.

        for r in range(len(s)):  # Expand window by moving right pointer.
            count[s[r]] = 1 + count.get(s[r], 0)  # Update frequency map.
            maxf = max(maxf, count[s[r]])  # Update max character frequency.

            # If the number of replacements needed is greater than `k`, shrink window.
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1  # Reduce count of character at `l`.
                l += 1  # Move `l` to shrink the window.

            res = max(res, r - l + 1)  # Update max window length.

        return res  # Return the longest valid substring length.
