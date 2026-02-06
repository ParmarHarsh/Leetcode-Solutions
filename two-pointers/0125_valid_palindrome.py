class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines whether a given string is a palindrome.

        The function ignores non-alphanumeric characters and is
        case-insensitive. It constructs a cleaned version of the
        string and then checks if it reads the same forwards and backwards.

        :param s: Input string to check
        :return: True if the string is a palindrome, otherwise False
        """

        # Build a new string containing only lowercase alphanumeric characters
        new_str = ""
        for ch in s:
            if ch.isalnum():
                new_str = new_str + ch.lower()

        # Initialize two pointers:
        # x_len starts from the beginning, y_len starts from the end
        x_len = 0
        y_len = len(new_str) - 1

        # Compare characters while moving inward from both ends
        while x_len < y_len:
            # If characters do not match, it is not a palindrome
            if new_str[x_len] != new_str[y_len]:
                return False

            # Move the pointers closer to the center
            x_len = x_len + 1
            y_len = y_len - 1

        # If all characters matched, the string is a palindrome
        return True

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — The string is traversed to clean it and then
        #        checked once using two pointers.
        #
        # Space Complexity:
        # O(n) — Extra space is used to store the cleaned string.
        # ---------------------------------------------------------
