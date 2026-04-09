from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Returns a valid order to complete all courses using Kahn’s Algorithm
        (Topological Sort via BFS).

        The algorithm works by:
        1. Computing the indegree (number of prerequisites) for each course.
        2. Starting with courses that have no prerequisites (indegree = 0).
        3. Repeatedly removing these courses and updating the indegrees
           of their dependent courses.

        If all courses are processed, a valid order exists.
        Otherwise, a cycle exists and no valid ordering is possible.

        :param numCourses: Total number of courses
        :param prerequisites: List of [course, prerequisite] pairs
        :return: A valid order of courses, or empty list if impossible
        """

        # indegree untuk simpan jumlah prasyarat tiap course
        indegree = [0] * numCourses

        # adjacency list untuk graph (pre -> list of courses)
        graph = [[] for _ in range(numCourses)]

        # bangun graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # queue untuk course tanpa prasyarat (indegree == 0)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        # list untuk menyimpan urutan hasil
        order = []

        # proses BFS
        while queue:
            # ambil course tanpa prasyarat
            cur = queue.popleft()
            order.append(cur)

            # kurangi indegree tetangga (courses dependent on current)
            for neighbor in graph[cur]:
                indegree[neighbor] -= 1

                # jika sudah tidak punya prasyarat, masukkan ke queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # kalau semua course bisa diambil, return order
        # jika tidak, berarti ada cycle → return []
        return order if len(order) == numCourses else []

        # ---------------------------------------------------------
        # Time Complexity:
        # O(V + E) — Each course and prerequisite is processed once.
        #
        # Space Complexity:
        # O(V + E) — Storage for graph and indegree array.
        # ---------------------------------------------------------