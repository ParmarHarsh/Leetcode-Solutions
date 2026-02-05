from typing import List
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines whether two strings are anagrams of each other.

        Two strings are anagrams if they contain the same characters
        with the same frequencies, possibly in a different order.

        :param s: First input string
        :param t: Second input string
        :return: True if the strings are anagrams, otherwise False
        """

        # If the lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Dictionaries to store character frequencies for each string
        dict_s = defaultdict(list)
        dict_t = defaultdict(list)

        # Iterate through both strings simultaneously by index
        for i in range(len(s)):
            # Increment the frequency count for the current character in s
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)

            # Increment the frequency count for the current character in t
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

        # Compare the two frequency dictionaries
        return dict_s == dict_t

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each character in the strings is processed once.
        #
        # Space Complexity:
        # O(n) — In the worst case, all characters are stored in the
        #        frequency dictionaries.
        # ---------------------------------------------------------
