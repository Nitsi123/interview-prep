from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Follow-up Questions:
        # 1. What should we return if `n` is 0? (Return the number of tasks since no cooldown is needed.)
        # 2. Can there be duplicate tasks in the list? (Yes, tasks may repeat.)
        # 3. What is the range of `n` and the number of tasks? (Assume both fit in memory.)
        # 4. Are tasks represented only as single characters or strings? (Assume single characters.)

        # Brute Force Approach:
        # - Simulate the execution of tasks using a list or queue.
        # - For each task, check if it can be scheduled based on cooldown constraints.
        # - If not, add idle time until the task can be executed.
        # - Time Complexity: O(n^2) in the worst case, if we have many tasks and need to iterate for idle periods.
        # - Space Complexity: O(n) to store tasks and cooldowns.

        # Optimized Approach:
        # - Use a max heap to keep track of the most frequent tasks.
        # - Use a queue to track tasks that are cooling down (not ready to be re-executed).
        # - Simulate the task execution:
        #   - Pop the most frequent task from the heap, decrement its count, and add it to the cooldown queue.
        #   - Push tasks back into the heap when their cooldown ends.
        #   - Keep track of time to return the total execution time.
        # - Time Complexity: O(n * log k), where `n` is the number of tasks and `k` is the number of unique tasks.
        # - Space Complexity: O(k), for the heap and cooldown queue.

        # Count the frequency of each task.
        counts = Counter(tasks)
        # Create a max heap (negative counts to simulate max heap with Python's min heap).
        maxheap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxheap)  # Convert the list into a heap.

        # Queue to store tasks that are cooling down, with their next available time.
        queue = deque()

        # Track the total time required to complete all tasks.
        time = 0

        # Process tasks until the heap and cooldown queue are empty.
        while maxheap or queue:
            time += 1  # Increment the time by 1 for each unit of task or idle time.

            # Execute the most frequent task if available.
            if maxheap:
                cnt = heapq.heappop(maxheap)  # Get the most frequent task.
                cnt += 1  # Decrement the count (negative count increases toward 0).
                if cnt:  # If there are more instances of this task, add it to the cooldown queue.
                    queue.append([cnt, time + n])

            # Check if any task in the cooldown queue is ready to be executed again.
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])  # Push the task back into the heap.

        return time  # Return the total time required.
