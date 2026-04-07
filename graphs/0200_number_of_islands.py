from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Counts the number of islands in a 2D grid.

        An island is formed by connecting adjacent lands ('1') horizontally or vertically.
        This implementation uses Breadth-First Search (BFS) to explore each island
        and mark all its cells as visited.

        :param grid: 2D list representing the map ('1' = land, '0' = water)
        :return: Number of islands
        """

        # Edge case: empty grid
        if not grid:
            return 0

        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Set to keep track of visited cells
        visit = set()

        # Counter for number of islands
        islands = 0

        def bfs(r, c):
            """
            Performs BFS to explore all connected land cells starting from (r, c).

            :param r: Row index
            :param c: Column index
            """

            # Initialize queue for BFS
            q = deque()

            # Mark the starting cell as visited
            visit.add((r, c))
            q.append((r, c))

            # Process the queue
            while q:
                row, col = q.popleft()

                # Possible directions: down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    # Calculate new coordinates
                    r = dr + row
                    c = dc + col

                    # Check bounds, land condition, and visited status
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visit
                    ):
                        q.append((r, c))
                        visit.add((r, c))

        # Traverse the entire grid
        for r in range(rows):
            for c in range(cols):

                # If cell is land and not visited, it's a new island
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
                else:
                    continue

        # Return total number of islands
        return islands

        # ---------------------------------------------------------
        # Time Complexity:
        # O(m * n) — Each cell is visited at most once.
        #
        # Space Complexity:
        # O(m * n) — In the worst case, the visited set and queue
        # may store all cells.
        # ---------------------------------------------------------