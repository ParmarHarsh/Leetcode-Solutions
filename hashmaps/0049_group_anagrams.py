from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups a list of strings into collections of anagrams.

        Strings are considered anagrams if they contain the same characters
        with the same frequencies. Each group contains strings that are
        anagrams of one another.

        :param strs: List of input strings
        :return: A list of lists, where each inner list contains anagrams
        """

        # Dictionary that maps a character frequency signature
        # to the list of strings matching that signature
        result = defaultdict(list)

        # Iterate through each string in the input list
        for ch in strs:
            # Create a frequency count for each character (a–z)
            cnt = [0] * 26

            # Count occurrences of each character in the string
            for c in ch:
                cnt[ord(c) - ord("a")] = cnt[ord(c) - ord("a")] + 1

            # Use the frequency count (as a tuple) as the key
            # and append the string to the corresponding group
            result[tuple(cnt)].append(ch)

        # Return all grouped anagrams as a list of lists
        return list(result.values())

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n * k) — n is the number of strings and k is the maximum
        #            length of a string (counting characters).
        #
        # Space Complexity:
        # O(n * k) — Storage for the hash map and character counts.
        # ---------------------------------------------------------
