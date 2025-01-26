from collections import Counter
from heapq import heappush, heappop, heapify

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Follow-up Questions:
        # 1. What should we return if it is not possible to reorganize the string? (Return an empty string `""`.)
        # 2. Can the input string contain non-alphabetic characters? (Assume only lowercase alphabetic characters.)
        # 3. Is the input string guaranteed to have a valid reorganization? (No, handle cases where reorganization is impossible.)
        # 4. What is the maximum length of the input string? (Assume it fits in memory.)

        # Optimized Approach:
        # - Use a max heap to always pick the character with the highest remaining count.
        # - Append the most frequent character to the result and temporarily store the previous character (used recently).
        # - After appending a character, decrease its count.
        # - Reinsert the previous character back into the heap only if its count is still positive.
        # - If at any point no valid reorganization is possible (e.g., one character count exceeds half the string length), return "".
        # - Time Complexity: O(n log k), where `n` is the length of the string, and `k` is the number of unique characters.
        # - Space Complexity: O(k), where `k` is the number of unique characters.

        # Step 1: Count the frequency of each character in the string.
        count = Counter(s)

        # Step 2: Create a max heap based on the frequency of characters.
        maxHeap = [[-cnt, char] for char, cnt in count.items()]  # Use negative counts for max heap.
        heapify(maxHeap)  # Convert the list into a heap.

        prev = None  # Store the previously used character.
        res = ""  # Initialize the result string.

        # Step 3: Process the heap to build the reorganized string.
        while maxHeap or prev:
            # If there are no characters left in the heap but `prev` still exists, return "" (impossible to reorganize).
            if prev and not maxHeap:
                return ""

            # Pop the most frequent character from the heap.
            cnt, char = heappop(maxHeap)

            # Append the character to the result string.
            res += char
            cnt += 1  # Decrease the count (negative count moves closer to 0).

            # Reinsert the previous character back into the heap if it still has a remaining count.
            if prev:
                heappush(maxHeap, prev)
                prev = None  # Reset `prev`.

            # If the current character still has a remaining count, store it as the previous character.
            if cnt != 0:
                prev = [cnt, char]

        return res  # Return the reorganized string.
