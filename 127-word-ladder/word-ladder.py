from typing import List
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Follow-up Questions:
        # 1. What should we return if `endWord` is not in the word list? (Return 0.)
        # 2. Are all words guaranteed to be of the same length? (Yes, assume they are.)
        # 3. Can there be duplicate words in the word list? (No, assume unique words.)
        # 4. Should the transformation be case-sensitive? (Yes, assume case-sensitive.)

        # Brute Force Approach:
        # - Perform a BFS without preprocessing:
        #   - For each word in the queue, generate all possible transformations by changing one character.
        #   - Check if each transformation exists in the word list and add it to the queue if valid.
        # - Time Complexity: O(n * m * 26), where `n` is the size of the word list, `m` is the word length, and 26 represents the alphabet size.
        # - Space Complexity: O(n + m), for the queue and word processing.

        # Optimized Approach:
        # - Preprocess the word list into a pattern-based adjacency list:
        #   - Create patterns by replacing each character in a word with `*` (e.g., `hot -> *ot, h*t, ho*`).
        #   - Store words matching each pattern in a hash map.
        # - Perform a BFS starting from `beginWord`:
        #   - For the current word, generate all patterns and access their neighbors in constant time.
        #   - Avoid revisiting words by using a `visit` set.
        #   - Return the number of steps if `endWord` is reached; otherwise, return 0.
        # - Time Complexity: O(n * m^2), where `n` is the size of the word list and `m` is the word length:
        #   - Preprocessing the word list takes O(n * m).
        #   - BFS processes up to `n` words, and for each word, generates `m` patterns and iterates over neighbors, costing O(m^2).
        # - Space Complexity: O(n * m), for the adjacency list and BFS queue.

        # Edge Case: If `endWord` is not in the word list, return 0.
        if endWord not in wordList:
            return 0

        # Step 1: Preprocess the word list to create an adjacency list based on patterns.
        nei = collections.defaultdict(list)
        wordList.append(beginWord)  # Add the `beginWord` to the word list.

        for word in wordList:
            for i in range(len(word)):
                # Create a pattern by replacing one character with `*`.
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word)

        # Step 2: Perform BFS starting from `beginWord`.
        q = collections.deque([beginWord])  # Queue to store words for BFS.
        visit = set([beginWord])  # Set to track visited words.
        res = 1  # Initialize the transformation length.

        while q:
            # Process all words at the current level.
            for i in range(len(q)):
                word = q.popleft()

                # If we reach the `endWord`, return the transformation length.
                if word == endWord:
                    return res

                # Explore all neighbors by matching patterns.
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)  # Mark the word as visited.
                            q.append(neiWord)  # Add the neighbor to the queue.

            res += 1  # Increment the transformation length for the next level.

        return 0  # If `endWord` is not reached, return 0.
