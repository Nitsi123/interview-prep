from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Follow-up Questions:
        # 1. What is the maximum size of the grid? (Assume it fits in memory.)
        # 2. Is the grid guaranteed to be rectangular? (Assume yes.)
        # 3. Can there be no land ("1") in the grid? (Yes, return 0 in this case.)
        # 4. Should diagonally connected land be counted as part of the same island? (No, only horizontal and vertical connections are valid.)

        # Brute Force Approach:
        # - Traverse the grid cell by cell.
        # - When a "1" (land) is found, initiate a depth-first search (DFS) or breadth-first search (BFS) to mark all connected land as visited.
        # - Increment the island count each time a new unvisited "1" is found.
        # - Time Complexity: O(m * n), where m is the number of rows and n is the number of columns (every cell is visited once).
        # - Space Complexity: O(m * n) in the worst case for the DFS/BFS stack if the grid is entirely land.

        # Optimized Approach:
        # - Use DFS (recursive) to traverse the grid and mark all connected land ("1") as visited by converting it to "0".
        # - Use a nested loop to traverse the entire grid.
        # - Each time a "1" is encountered, start a DFS to mark the entire connected component as visited.
        # - Increment the count of islands for each new DFS initiated.
        # - Time Complexity: O(m * n), as each cell is visited once.
        # - Space Complexity: O(m * n), due to the recursion stack in the worst case.

        count = 0  # Initialize the count of islands

        def dfs(grid, i, j):
            # Perform a depth-first search to mark connected land as visited.
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return  # Return if out of bounds or the cell is water ("0").
            
            grid[i][j] = "0"  # Mark the current cell as visited by setting it to "0".
            # Recursively visit all adjacent cells (up, down, left, right).
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        # Traverse the grid row by row and column by column.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # If the current cell is land ("1"):
                    dfs(grid, i, j)  # Perform DFS to mark the entire island as visited.
                    count += 1  # Increment the island count.

        return count  # Return the total number of islands.
