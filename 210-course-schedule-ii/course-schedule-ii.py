from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Follow-up Questions:
        # 1. What should we return if it is impossible to complete all courses? (Return an empty list `[]`.)
        # 2. Are the courses labeled from 0 to numCourses - 1? (Yes, assume they are.)
        # 3. Can there be duplicate prerequisites? (Assume no, each pair is unique.)
        # 4. Is it guaranteed that all courses are connected? (No, handle disconnected components as well.)

        # Optimized Approach:
        # - Use a graph representation (adjacency list) to map each course to its prerequisites.
        # - Perform a depth-first search (DFS) to detect cycles and determine the course order:
        #   - Use a `cycle` set to track nodes in the current DFS path.
        #   - Use a `visit` set to track nodes that have been fully processed.
        #   - Add courses to the result in reverse order (postorder traversal).
        # - Time Complexity: O(V + E), where `V` is the number of courses and `E` is the number of prerequisites.
        # - Space Complexity: O(V + E), for the graph representation and recursion stack.

        # Step 1: Build an adjacency list to represent the prerequisite graph.
        premap = {i: [] for i in range(numCourses)}  # Initialize adjacency list.
        for crs, pre in prerequisites:
            premap[crs].append(pre)  # Add prerequisite for the course.

        visit, cycle = set(), set()  # `visit` tracks fully processed nodes; `cycle` tracks current DFS path.
        res = []  # List to store the course order.

        # Step 2: Define a DFS function to detect cycles and determine the order.
        def dfs(crs):
            if crs in cycle:  # If the course is in the current path, a cycle is detected.
                return False
            
            if crs in visit:  # If the course is already processed, skip it.
                return True
            
            cycle.add(crs)  # Add the course to the current DFS path.

            # Recursively process all prerequisites of the current course.
            for pre in premap[crs]:
                if not dfs(pre):  # If a cycle is detected, return False.
                    return False

            cycle.remove(crs)  # Remove the course from the current DFS path.
            visit.add(crs)  # Mark the course as fully processed.
            res.append(crs)  # Add the course to the result (postorder).

            return True

        # Step 3: Perform DFS for each course to determine the order.
        for crs in range(numCourses):
            if not dfs(crs):  # If a cycle is detected, return an empty list.
                return []

        # Step 4: Return the reversed result list to get the correct course order.
        return res
