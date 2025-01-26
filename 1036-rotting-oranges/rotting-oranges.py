from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Follow-up Questions:
        # 1. What should we return if there are no fresh oranges? (Return 0.)
        # 2. What if the grid contains no oranges at all? (Return 0.)
        # 3. Can the grid contain invalid values? (Assume no, input is valid.)
        # 4. What is the maximum size of the grid? (Assume it fits in memory.)

        # Brute Force Approach:
        # - Simulate the rotting process step-by-step:
        #   - For every minute, iterate over the entire grid and find all rotten oranges.
        #   - For each rotten orange, rot its adjacent fresh oranges.
        #   - Repeat the process until no fresh orange can be rotted.
        # - Time Complexity: O((m * n)^2), where `m` and `n` are the grid dimensions. Each step requires traversing the entire grid.
        # - Space Complexity: O(1), as no extra data structures are used.

        # Optimized Approach:
        # - Use a breadth-first search (BFS) to simulate the rotting process:
        #   - Add all initially rotten oranges to a queue.
        #   - Keep a count of fresh oranges.
        #   - For each rotten orange, rot its adjacent fresh oranges and decrement the fresh orange count.
        #   - Track the time required for all fresh oranges to rot.
        #   - If any fresh orange remains at the end, return -1.
        # - Time Complexity: O(m * n), as each cell is processed at most once.
        # - Space Complexity: O(m * n), for the queue used in BFS.

        time = 0  # Initialize the time required for all oranges to rot.
        fresh = 0  # Count of fresh oranges.
        deque = collections.deque()  # Queue to store the coordinates of rotten oranges.

        # Step 1: Initialize the queue with all rotten oranges and count fresh oranges.
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:  # Fresh orange.
                    fresh += 1
                if grid[r][c] == 2:  # Rotten orange.
                    deque.append((r, c))

        # Step 2: Define the directions for moving up, down, left, and right.
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 3: Perform BFS to rot adjacent fresh oranges.
        while deque and fresh:
            for i in range(len(deque)):
                r, c = deque.popleft()  # Get the current rotten orange.

                # Process all adjacent cells.
                for dir in dirs:
                    new_r = r + dir[0]
                    new_c = c + dir[1]

                    # Skip invalid or non-fresh cells.
                    if new_r < 0 or new_c < 0 or new_r >= len(grid) or new_c >= len(grid[0]) or grid[new_r][new_c] != 1:
                        continue

                    # Rot the fresh orange and add it to the queue.
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    deque.append((new_r, new_c))

            # Increment time after processing all oranges at the current level.
            time += 1

        # Step 4: If there are still fresh oranges left, return -1.
        if fresh > 0:
            return -1

        # Step 5: Return the total time taken for all oranges to rot.
        return time
