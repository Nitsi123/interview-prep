class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Follow-up Questions:
        # 1. What should we return if the input string is empty? (Return an empty string `""`.)
        # 2. Should the solution be case-sensitive? (Yes, "A" and "a" are considered different characters.)
        # 3. Can the input string contain special characters or spaces? (Yes, handle them as part of the string.)
        # 4. What is the maximum length of the input string? (Assume it fits in memory.)

        # Brute Force Approach:
        # - Iterate through all substrings of the input string.
        # - For each substring, check if it is a palindrome:
        #   - Reverse the substring and compare it to the original.
        #   - If it is a palindrome, compare its length with the maximum length found so far.
        # - Return the longest palindromic substring.
        # - Time Complexity: O(n^3), where `n` is the length of the string (O(n^2) for generating substrings and O(n) for checking each substring).
        # - Space Complexity: O(n), to store each substring.

        # Optimized Approach:
        # - Use a center-expansion technique to check for palindromes:
        #   - Expand around each character to find odd-length palindromes.
        #   - Expand around each pair of adjacent characters to find even-length palindromes.
        # - Update the result if the length of the current palindrome is greater than the previous maximum length.
        # - Time Complexity: O(n^2), where `n` is the length of the string (each character is expanded up to `n` times).
        # - Space Complexity: O(1), as no extra space is used apart from variables.

        res = ""  # Initialize the result to store the longest palindrome.
        resLen = 0  # Initialize the maximum length of the palindrome.

        # Iterate through each character in the string.
        for i in range(len(s)):
            # Check for odd-length palindromes centered at `i`.
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update the result if the current palindrome is longer than the previous one.
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1  # Expand left.
                r += 1  # Expand right.

            # Check for even-length palindromes centered between `i` and `i + 1`.
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update the result if the current palindrome is longer than the previous one.
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1  # Expand left.
                r += 1  # Expand right.

        return res  # Return the longest palindromic substring.
