from sortedcontainers import SortedDict


class TimeMap:
    """
    Time-based key-value store that supports setting and retrieving values
    based on timestamps.

    Each key maps to a SortedDict where:
    - Keys are timestamps
    - Values are the corresponding stored values

    This allows efficient retrieval of the most recent value
    at or before a given timestamp.
    """

    def __init__(self):
        """
        Initializes the TimeMap with an empty dictionary.
        """
        # Dictionary mapping keys to their SortedDict of (timestamp -> value)
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key with the given value at the specified timestamp.

        :param key: The key to store
        :param value: The value associated with the key
        :param timestamp: The timestamp at which the value is stored
        """

        # If the key does not exist, initialize a SortedDict for it
        if key not in self.map:
            self.map[key] = SortedDict()

        # Insert the timestamp-value pair into the SortedDict
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieves the value associated with the largest timestamp
        less than or equal to the given timestamp.

        :param key: The key to retrieve
        :param timestamp: The timestamp to query
        :return: The corresponding value, or "" if none exists
        """

        # If the key does not exist, return empty string
        if key not in self.map:
            return ""

        # Find the insertion index for the given timestamp
        i = self.map[key].bisect_right(timestamp)

        # If index is 0, no valid timestamp exists
        if i == 0:
            return ""

        # Retrieve the value at the largest timestamp <= given timestamp
        return self.map[key].peekitem(i - 1)[1]

    # ---------------------------------------------------------
    # Time Complexity:
    # set: O(log n) — Insertion into SortedDict.
    # get: O(log n) — Binary search via bisect.
    #
    # Space Complexity:
    # O(n) — Stores all key-timestamp-value entries.
    # ---------------------------------------------------------


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)