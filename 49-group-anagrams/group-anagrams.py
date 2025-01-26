from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Follow-up Questions:
        # 1. Can the input list be empty? (Yes, return an empty list `[]`.)
        # 2. Are the input strings guaranteed to contain only lowercase letters? (Yes, assume lowercase alphabetic characters.)
        # 3. Can strings have varying lengths? (Yes, handle accordingly.)
        # 4. Should the result maintain the order of the input strings? (Order within groups is maintained, but group order can vary.)

        # Optimized Approach:
        # - Use a hash map (`res`) to group anagrams.
        # - For each string, calculate a unique signature based on the frequency of characters.
        #   - Use an array of size 26 to count the occurrences of each letter in the string.
        #   - Convert the count array into a tuple (immutable) to use it as a key in the hash map.
        # - Append the string to the corresponding group in the hash map.
        # - Time Complexity: O(n * k), where `n` is the number of strings and `k` is the maximum string length.
        # - Space Complexity: O(n * k), to store the strings and their groups in the hash map.

        # Initialize a dictionary to group anagrams. Keys are character frequency tuples, and values are lists of strings.
        res = defaultdict(list)

        # Iterate through each string in the input list.
        for s in strs:
            # Create a character frequency array of size 26 (for 'a' to 'z').
            count = [0] * 26

            # Count the frequency of each character in the string.
            for c in s:
                count[ord(c) - ord("a")] += 1

            # Use the tuple of the count array as a key and append the string to the corresponding group.
            res[tuple(count)].append(s)

        # Return the grouped anagrams as a list of lists.
        return list(res.values())
