class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring that can be obtained
        by replacing at most k characters in the string so that all
        characters in the substring are the same.

        The function uses a sliding window approach and keeps track
        of character frequencies within the current window.

        :param s: Input string consisting of uppercase English letters
        :param k: Maximum number of character replacements allowed
        :return: Length of the longest valid substring
        """

        # Dictionary to store the frequency of characters in the current window
        my_map = {}

        # Left pointer of the sliding window
        l = 0

        # Variable to store the maximum valid substring length found
        result = 0

        # Iterate with the right pointer expanding the window
        for r in range(0, len(s)):
            # Increment the count of the current character
            my_map[s[r]] = 1 + my_map.get(s[r], 0)

            # Check if the current window is valid
            # If the number of characters to replace exceeds k,
            # shrink the window from the left
            while ((r - l + 1) - max(my_map.values())) > k:
                my_map[s[l]] = my_map[s[l]] - 1
                l += 1

            # Update the maximum length found so far
            result = max(result, r - l + 1)

        # Return the length of the longest valid substring
        return result

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n * 26) ≈ O(n) — Each character is processed once,
        # and max(my_map.values()) runs in constant time since
        # the alphabet size is limited.
        #
        # Space Complexity:
        # O(1) — At most 26 characters are stored in the dictionary.
        # ---------------------------------------------------------
