# Brute Force Approach:
# Concatenate both words character-by-character by iterating over both
# strings and appending characters alternately to the result.
# If one string is shorter, append its characters followed by the remaining
# characters of the longer string at the end.
# Time Complexity: O(n + m), where n and m are the lengths of word1 and word2.
# Space Complexity: O(n + m), as we store the concatenated result in a new string.

# Optimized Approach:
# Use two pointers to alternate characters from each string and build the result list.
# 1. Initialize two pointers, `i` for `word1` and `j` for `word2`, and an empty list `res` to store the merged characters.
# 2. While both pointers are within the bounds of their respective strings:
#    - Append the character at `i` from `word1` and the character at `j` from `word2` to `res`.
#    - Increment both `i` and `j` to move to the next characters.
# 3. Once one of the strings is exhausted, append the remaining characters of the other string.
# 4. Finally, join the list `res` into a single string and return it.

from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []  # List to store the alternating characters
        i, j = 0, 0  # Initialize pointers for both strings

        # Alternate characters from both strings while both have characters remaining
        while i < len(word1) and j < len(word2):
            res.append(word1[i])  # Append character from word1
            res.append(word2[j])  # Append character from word2
            i += 1  # Move to the next character in word1
            j += 1  # Move to the next character in word2
        
        # Append any remaining characters from word1 or word2
        res.append(word1[i:])  # Append remaining characters of word1, if any
        res.append(word2[j:])  # Append remaining characters of word2, if any
        
        return "".join(res)  # Join the list into a single string and return

# Time Complexity: O(n + m), where n and m are the lengths of word1 and word2, respectively,
# as we iterate through both words once.
# Space Complexity: O(n + m), as we store the characters in a list before joining.