from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Follow-up Questions:
        # 1. Can `s1` or `s2` contain uppercase letters? (No, assume all lowercase.)
        # 2. Can `s1` be longer than `s2`? (Yes, but return `False` immediately.)
        # 3. Do we need to find all permutations? (No, return `True` if at least one exists.)
        # 4. What if `s1` is empty? (Edge case, assume `False` is returned.)

        # Brute Force Approach:
        # - Generate all permutations of `s1`.
        # - Check if any permutation is a substring of `s2`.
        # - Time Complexity: O(n! * m), since generating permutations is expensive.
        # - Space Complexity: O(n!), storing all permutations.

        # Optimized Approach (Sliding Window with Frequency Count):
        # - Use an array of size 26 to store frequency counts of `s1` and `s2`.
        # - Maintain a **sliding window of size `len(s1)`** over `s2`:
        #   - If character counts match, return `True`.
        #   - Slide the window by updating frequencies.
        # - Time Complexity: O(n), since we only iterate through `s2` once.
        # - Space Complexity: O(1), since arrays are fixed at size 26.

        if len(s1) > len(s2):  # Edge case: s1 longer than s2.
            return False
        
        s1Count = [0] * 26  # Frequency count of `s1`.
        s2Count = [0] * 26  # Frequency count for sliding window in `s2`.
        
        for i in range(len(s1)):  # Initialize frequency counts.
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
        
        matches = sum(1 for i in range(26) if s1Count[i] == s2Count[i])  # Count matches.

        l = 0  # Left pointer for sliding window.
        for r in range(len(s1), len(s2)):  # Expand right pointer.
            if matches == 26:  # If all frequencies match, we found a permutation.
                return True
            
            # Add new character to window.
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1

            # Update match count based on new character.
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:  # If it was previously matching but now exceeds.
                matches -= 1
            
            # Remove old character from window.
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1

            # Update match count based on removed character.
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:  # If it was previously matching but now decreases.
                matches -= 1
            
            l += 1  # Move left pointer.

        return matches == 26  # Check for final match.
