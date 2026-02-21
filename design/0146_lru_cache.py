class Node:
    """
    Node class for the doubly linked list used in LRUCache.

    Each node stores:
    - key: The cache key
    - value: The associated value
    - prev: Pointer to the previous node
    - next: Pointer to the next node
    """

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    Implements a Least Recently Used (LRU) Cache.

    The cache uses:
    - A dictionary (hash map) for O(1) access to nodes.
    - A doubly linked list to maintain usage order.
      - Most recently used (MRU) items are placed near the head.
      - Least recently used (LRU) items are near the tail.
    """

    def __init__(self, capacity: int):
        """
        Initializes the LRUCache with a given capacity.

        :param capacity: Maximum number of items the cache can hold
        """

        self.capacity = capacity

        # Dictionary mapping keys to their corresponding nodes
        self.cache = {}

        # Dummy head and tail nodes to simplify insert/remove operations
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # Initialize empty doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """
        Removes a node from the doubly linked list.

        :param node: Node to be removed
        """

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node: Node):
        """
        Inserts a node right after the head (marking it as most recently used).

        :param node: Node to insert
        """

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """
        Retrieves the value associated with the key if it exists.
        Marks the accessed node as most recently used.

        :param key: Key to retrieve
        :return: Value if key exists, otherwise -1
        """

        if key in self.cache:
            node = self.cache[key]

            # Move the accessed node to the front (MRU position)
            self._remove(node)
            self._insert(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a key-value pair in the cache.
        If the cache exceeds capacity, removes the least recently used item.

        :param key: Key to insert/update
        :param value: Value to associate with the key
        """

        # If key already exists, remove the old node
        if key in self.cache:
            self._remove(self.cache[key])

        # Create a new node and insert it at the front
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        # If capacity is exceeded, remove the least recently used node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev

            self._remove(lru)
            del self.cache[lru.key]

    # ---------------------------------------------------------
    # Time Complexity:
    # get: O(1)
    # put: O(1)
    #
    # Space Complexity:
    # O(capacity) — Stores up to `capacity` elements in the cache.
    # ---------------------------------------------------------


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)