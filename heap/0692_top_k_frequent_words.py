from typing import List
import heapq


class Solution:
    def MyCmp(self, x):
        """
        Custom comparator function used for heap ordering.

        It sorts primarily by:
        - Frequency in descending order (higher frequency first)
        - Word in ascending lexicographical order (for ties)

        :param x: Tuple of (word, frequency)
        :return: Tuple used for comparison in heap operations
        """
        return -x[1], x[0]

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Finds the k most frequent words in the list.

        Words are sorted by:
        1. Frequency (descending)
        2. Lexicographical order (ascending) for ties

        The function uses a dictionary to count frequencies and
        heapq.nsmallest with a custom comparator to retrieve
        the top k frequent words.

        :param words: List of input words
        :param k: Number of most frequent words to return
        :return: List of k most frequent words
        """

        # Dictionary to store frequency of each word
        wordsDict = {}

        # Count occurrences of each word
        for w in words:
            if w not in wordsDict:
                wordsDict[w] = 1
            else:
                wordsDict[w] += 1

        # Build a list of (word, frequency) pairs
        # and use nsmallest with custom comparator to get top k
        result = heapq.nsmallest(
            k,
            [(n[0], n[1]) for n in wordsDict.items()],
            key=self.MyCmp
        )

        # Extract only the words from the result
        return [r[0] for r in result]

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n log k) — Counting takes O(n), and heap operations
        #              take O(log k) per insertion.
        #
        # Space Complexity:
        # O(n) — Stores frequency dictionary and intermediate list.
        # ---------------------------------------------------------