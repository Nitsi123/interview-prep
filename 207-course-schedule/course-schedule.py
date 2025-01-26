from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Follow-up Questions:
        # 1. Can there be duplicate prerequisites? (Assume no; each pair is unique.)
        # 2. Can the prerequisites form a cyclic dependency? (Yes, handle cycles properly.)
        # 3. Is it guaranteed that all course indices are between 0 and numCourses-1? (Yes.)
        # 4. What should we return if there are no prerequisites? (Return True, as all courses can be taken.)

        # Brute Force Approach:
        # - Use a depth-first search (DFS) for each course to detect cycles.
        # - For every course, recursively check its prerequisites and see if there is a back edge (cycle).
        # - Time Complexity: O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges).
        # - Space Complexity: O(V + E), for the adjacency list and recursion stack.

        # Optimized Approach:
        # - Represent the course prerequisites as a graph using an adjacency list.
        # - Use DFS with a `visit` set to detect cycles:
        #   - If a course is revisited while in the same DFS path, it means there’s a cycle.
        #   - If a course has no prerequisites or all prerequisites are resolved, mark it as completed.
        # - Time Complexity: O(V + E), as every course and prerequisite is processed once.
        # - Space Complexity: O(V + E), for the adjacency list and recursion stack.

        # Step 1: Build an adjacency list to represent the course prerequisite graph.
        premap = {i: [] for i in range(numCourses)}  # Initialize adjacency list.
        for crs, pre in prerequisites:
            premap[crs].append(pre)  # Add prerequisite for the course.

        # Step 2: Define a DFS function to detect cycles.
        def dfs(crs):
            if crs in visit:  # If the course is in the current DFS path, a cycle is detected.
                return False
            
            if premap[crs] == []:  # If the course has no prerequisites, it is already resolved.
                return True
            
            visit.add(crs)  # Mark the course as visited in the current DFS path.

            # Recursively check all prerequisites for the current course.
            for pre in premap[crs]:
                if not dfs(pre):
                    return False  # If any prerequisite causes a cycle, return False.

            visit.remove(crs)  # Remove the course from the current DFS path.
            premap[crs] = []  # Mark the course as resolved (no unresolved prerequisites).
            return True

        # Step 3: Use a set to track courses in the current DFS path.
        visit = set()

        # Step 4: Perform DFS for each course to ensure all courses can be completed.
        for c in range(numCourses):
            if not dfs(c):  # If any course cannot be completed, return False.
                return False

        return True  # If all courses can be completed, return True.
