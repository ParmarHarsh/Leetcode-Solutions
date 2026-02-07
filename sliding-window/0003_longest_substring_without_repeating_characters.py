class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        This function uses a sliding window approach with two pointers and a set
        to track unique characters in the current window.

        :param s: Input string
        :return: Length of the longest substring without repeating characters
        """

        # Left pointer of the sliding window
        x = 0

        # Right pointer of the sliding window
        y = 0

        # Set to store unique characters in the current window
        my_set = set()

        # Variable to store the maximum length found
        length = 0

        # Iterate until the right pointer reaches the end of the string
        while x < len(s):
            # If the current character is not in the set,
            # expand the window to the right
            if s[x] not in my_set:
                my_set.add(s[x])

                # Update the maximum length if needed
                length = max(length, x - y + 1)

                # Move the right pointer forward
                x = x + 1
            else:
                # If a duplicate character is found,
                # shrink the window from the left
                my_set.remove(s[y])
                y = y + 1

        # Return the maximum length found
        return length

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each character is added to and removed from the set
        #        at most once.
        #
        # Space Complexity:
        # O(n) — In the worst case, the set stores all unique characters.
        # ---------------------------------------------------------
