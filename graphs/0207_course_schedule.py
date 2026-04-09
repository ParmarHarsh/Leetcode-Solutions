from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if it is possible to finish all courses given the prerequisites.

        This problem is equivalent to detecting a cycle in a directed graph.
        Each course is a node, and prerequisites form directed edges.

        The solution uses Depth-First Search (DFS) with cycle detection:
        - If a node is revisited during the same DFS path, a cycle exists.
        - If no cycles are found, all courses can be completed.

        :param numCourses: Total number of courses
        :param prerequisites: List of [course, prerequisite] pairs
        :return: True if all courses can be finished, otherwise False
        """

        # Build adjacency list (course -> list of prerequisites)
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Set to track nodes in the current DFS path (cycle detection)
        visited = set()

        def dfs(crs):
            """
            Performs DFS to detect cycles.

            :param crs: Current course
            :return: False if a cycle is detected, otherwise True
            """

            # If course is already in the current path, cycle detected
            if crs in visited:
                return False

            # If no prerequisites, course can be completed
            if preMap[crs] == []:
                return True

            # Mark the course as visited in current path
            visited.add(crs)

            # Visit all prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # Remove course from current path after processing
            visited.remove(crs)

            # Mark course as completed by clearing prerequisites
            preMap[crs] = []

            return True

        # Check all courses
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

        # ---------------------------------------------------------
        # Time Complexity:
        # O(V + E) — Each course and prerequisite is processed once.
        #
        # Space Complexity:
        # O(V + E) — Adjacency list and recursion stack.
        # ---------------------------------------------------------