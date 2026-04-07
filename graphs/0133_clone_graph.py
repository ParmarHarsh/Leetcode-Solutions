from typing import Optional


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Creates a deep copy (clone) of an undirected graph.

        This implementation uses Depth-First Search (DFS) with a hashmap
        to keep track of already cloned nodes to avoid infinite loops
        in cyclic graphs.

        :param node: A reference node in the original graph
        :return: A deep copy of the graph
        """

        # Dictionary to map original nodes to their clones
        clones = {}

        def solve(node):
            """
            Recursively clones the graph using DFS.

            :param node: Current node being processed
            :return: Cloned node
            """

            # Create a clone of the current node
            new_ = Node(node.val)

            # Store the mapping from original node to cloned node
            clones[node] = new_

            # Iterate through all neighbors of the current node
            for vertex in node.neighbors:

                # If the neighbor is already cloned, use it directly
                if vertex in clones:
                    new_.neighbors.append(clones[vertex])

                else:
                    # Otherwise, recursively clone the neighbor
                    new_.neighbors.append(solve(vertex))

            # Return the cloned node
            return new_

        # Edge case: if input node is None
        if not node:
            return None

        # Start DFS cloning from the given node
        return solve(node)

        # ---------------------------------------------------------
        # Time Complexity:
        # O(V + E) — Each node and edge is visited once.
        #
        # Space Complexity:
        # O(V) — Hashmap stores all nodes, recursion stack may also grow to O(V).
        # ---------------------------------------------------------