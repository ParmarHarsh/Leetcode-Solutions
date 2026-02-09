class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Determines whether a string can be a palindrome after deleting
        at most one character.

        The function first checks if the string is already a palindrome.
        If not, it uses a two-pointer approach to find the first mismatch
        and then checks whether removing either the left or right character
        results in a palindrome.

        :param s: Input string
        :return: True if the string can be a palindrome after at most one deletion,
                 otherwise False
        """

        def isPalindrome(s: str):
            """
            Helper function to check if a given string is a palindrome.

            :param s: Input string
            :return: True if the string is a palindrome, otherwise False
            """
            if s == s[::-1]:
                return True
            else:
                return False

        # If the original string is already a palindrome, return True
        if isPalindrome(s):
            return True

        # Initialize two pointers at the beginning and end of the string
        left = 0
        right = len(s) - 1

        # Move pointers inward while characters match
        while s[left] == s[right]:
            left += 1
            right -= 1

        # Check if removing either the left or right character
        # results in a palindrome
        return (
            isPalindrome(s[:left] + s[left + 1:])
            or isPalindrome(s[:right] + s[right + 1:])
        )

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — The string is traversed with two pointers, and
        #        palindrome checks take linear time.
        #
        # Space Complexity:
        # O(n) — Extra space is used for substring creation.
        # ---------------------------------------------------------
