from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Follow-up Questions:
        # 1. Can the input list of intervals be empty? (Yes, return an empty list.)
        # 2. Are the intervals guaranteed to be sorted? (No, sort them by their start times.)
        # 3. Can the intervals overlap partially or completely? (Yes, merge them when they overlap.)
        # 4. Are the intervals always valid, with `start <= end`? (Yes, assume they are valid.)

        # Brute Force Approach:
        # - Compare every interval with every other interval to check for overlaps.
        # - Merge overlapping intervals and repeat the process until no more overlaps exist.
        # - Time Complexity: O(n^2), as every interval is compared with every other interval.
        # - Space Complexity: O(n), as a new list is created to store merged intervals.

        # Optimized Approach:
        # - Sort the intervals by their start times.
        # - Iterate through the sorted intervals and merge overlapping intervals:
        #   - If the current interval overlaps with the last interval in the result, merge them.
        #   - Otherwise, add the current interval to the result.
        # - Time Complexity: O(n log n), for sorting the intervals.
        # - Space Complexity: O(n), for the result list.

        if not intervals:  # Edge case: If the input list is empty, return an empty list.
            return []

        # Step 1: Sort the intervals by their start times.
        intervals.sort(key=lambda x: x[0])

        # Initialize the result list with the first interval.
        res = [intervals[0]]

        # Step 2: Traverse the sorted intervals and merge overlapping intervals.
        for i in range(1, len(intervals)):
            # Check if the current interval overlaps with the last interval in the result.
            if res[-1][1] >= intervals[i][0]:
                # Merge the intervals by updating the end time of the last interval.
                curr = res.pop()  # Remove the last interval temporarily.
                curr_min = min(curr[0], intervals[i][0])  # Get the minimum start time.
                curr_max = max(curr[1], intervals[i][1])  # Get the maximum end time.
                res.append([curr_min, curr_max])  # Add the merged interval to the result.
            else:
                # If no overlap, add the current interval to the result.
                res.append(intervals[i])

        return res  # Return the merged intervals.
