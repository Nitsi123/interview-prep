# Brute Force / Optimized Approach:
# Take the first string as a reference and compare each character of this string with
# corresponding characters in all other strings.
# If all strings match at a particular character index, add this character to the result.
# If any string differs, stop and return the common prefix found so far.

# Time Complexity: O(n * m), where n is the number of strings and m is the length of the shortest string.
# Space Complexity: O(m), where m is the length of the common prefix.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""  # Initialize result to store common prefix

        for i in range(len(strs[0])):  # Iterate through each character of the first string
            for s in strs[1:]:  # Check the character at index i in each string
                if i == len(s) or s[i] != strs[0][i]:  # If any str is shorter or has a diff. char.
                    return res  # Return the common prefix found so far
            res += strs[0][i]  # If all strs have the same char, add it to result
        
        return res  # Return the longest common prefix