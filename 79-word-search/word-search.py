from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Follow-up Questions:
        # 1. What should we return if the board is empty? (Return False.)
        # 2. Can the word contain duplicate characters? (Yes, assume it can.)
        # 3. Can the board contain only a subset of the word's characters? (Yes, handle accordingly.)
        # 4. Is the search case-sensitive? (Yes, assume it is case-sensitive.)
        # 5. Can the same cell be used more than once in the search? (No, a cell can only be used once per word.)

        # Brute Force Approach:
        # - Iterate through every cell of the board.
        # - For each cell, start a depth-first search (DFS) to find the word.
        # - If the DFS successfully matches the word, return True; otherwise, continue.
        # - Time Complexity: O((m * n) * 4^k), where `m` and `n` are the dimensions of the board, and `k` is the length of the word.
        # - Space Complexity: O(k), for the recursion stack, where `k` is the length of the word.

        # Optimized Approach:
        # - Use DFS with backtracking to traverse the board.
        # - Mark cells as visited during the DFS and restore them after recursion.
        # - Prune unnecessary searches by returning early if the word cannot be matched.
        # - Time Complexity: O((m * n) * 4^k), where `m` and `n` are the dimensions of the board, and `k` is the length of the word.
        # - Space Complexity: O(k), for the recursion stack, where `k` is the length of the word.

        if not board:  # Edge case: If the board is empty, return False.
            return False

        def dfs(i, j, word):
            # Base case: If the word is fully matched, return True.
            if len(word) == 0:
                return True
            
            # Check for out-of-bounds conditions or mismatched characters.
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
                return False
            
            # Temporarily mark the current cell as visited.
            temp = board[i][j]
            board[i][j] = '#'

            # Recursively search in all four directions (up, down, left, right).
            res = (
                dfs(i + 1, j, word[1:]) or
                dfs(i - 1, j, word[1:]) or
                dfs(i, j + 1, word[1:]) or
                dfs(i, j - 1, word[1:])
            )
            
            # Restore the current cell after the search.
            board[i][j] = temp
            return res

        # Iterate through every cell in the board to start the search.
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Start a DFS search if the current cell matches the first character of the word.
                if dfs(i, j, word):
                    return True

        return False  # Return False if the word cannot be found.
