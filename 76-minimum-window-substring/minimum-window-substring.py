from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Follow-up Questions:
        # 1. Can `t` be longer than `s`? (Yes, but return `""` immediately.)
        # 2. Can `t` contain characters not in `s`? (Yes, but return `""` immediately.)
        # 3. Are there multiple valid minimum windows? (No, the problem guarantees a unique answer.)
        # 4. What if `t` is empty? (Return `""` as there's nothing to match.)

        # Brute Force Approach:
        # - Generate all possible substrings of `s`.
        # - For each substring, check if it contains all characters of `t` with correct frequencies.
        # - Track the shortest valid substring.
        # - Time Complexity: O(n^3), due to generating substrings and frequency checks.
        # - Space Complexity: O(1), aside from input and output storage.

        # Optimized Approach (Sliding Window with Hash Maps):
        # - Use two hash maps:
        #   - `countT`: Frequency of characters in `t`.
        #   - `window`: Frequency of characters in the current window of `s`.
        # - Expand the window by moving the right pointer (`r`).
        # - Once the window contains all characters of `t`:
        #   - Contract the window by moving the left pointer (`l`) to find the minimum length.
        # - Track the minimum window length and its boundaries.
        # - Time Complexity: O(n), since both pointers traverse `s` once.
        # - Space Complexity: O(|t| + |s|), due to the hash maps.

        if not t or not s:
            return ""
        
        countT = Counter(t)  # Frequency map for `t`.
        window = {}  # Frequency map for the current window in `s`.

        have, need = 0, len(countT)  # `have` tracks how many characters match the required frequency.
        res, resLen = [-1, -1], float("inf")  # To store the result window's boundaries and length.
        l = 0  # Left pointer of the window.

        # Expand the window with the right pointer `r`.
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # Check if current character's frequency matches the required frequency in `t`.
            if char in countT and window[char] == countT[char]:
                have += 1

            # Contract the window from the left until it ceases to be valid.
            while have == need:
                # Update result if this window is smaller.
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Pop the leftmost character from the window.
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1  # Move left pointer to the right.

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
