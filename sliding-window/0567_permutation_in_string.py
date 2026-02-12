class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Determines if s2 contains a permutation of s1.

        The function uses a sliding window approach with fixed-size
        frequency arrays (size 26 for lowercase letters) to compare
        character counts between s1 and the current window in s2.

        :param s1: String whose permutation we are looking for
        :param s2: String in which we search for a permutation of s1
        :return: True if any permutation of s1 exists in s2, otherwise False
        """

        # If s1 is longer than s2, no permutation is possible
        if len(s1) > len(s2):
            return False

        # Frequency count arrays for s1 and the current window in s2
        s1_cnt = [0] * 26
        s2_cnt = [0] * 26

        # Initialize frequency counts for the first window
        for i in range(len(s1)):
            s1_cnt[ord(s1[i]) - ord('a')] = (
                s1_cnt[ord(s1[i]) - ord('a')] + 1
            )
            s2_cnt[ord(s2[i]) - ord('a')] = (
                s2_cnt[ord(s2[i]) - ord('a')] + 1
            )

        # Count how many character frequencies match exactly
        matches = 0
        for i in range(26):
            x = 0
            if s1_cnt[i] == s2_cnt[i]:
                x = 1
            matches += x

        # Left pointer for the sliding window
        l = 0

        # Slide the window across s2
        for r in range(len(s1), len(s2)):
            # If all 26 character counts match, a permutation is found
            if matches == 26:
                return True

            # Add the new character on the right to the window
            index = ord(s2[r]) - ord('a')
            s2_cnt[index] = s2_cnt[index] + 1

            # Update matches based on the new count
            if s1_cnt[index] == s2_cnt[index]:
                matches += 1
            elif s1_cnt[index] + 1 == s2_cnt[index]:
                matches -= 1

            # Remove the leftmost character from the window
            index = ord(s2[l]) - ord('a')
            s2_cnt[index] = s2_cnt[index] - 1

            # Update matches after removal
            if s1_cnt[index] == s2_cnt[index]:
                matches += 1
            elif s1_cnt[index] - 1 == s2_cnt[index]:
                matches -= 1

            # Move the left pointer forward
            l += 1

        # Final check after the loop ends
        return matches == 26

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each character in s2 is processed once.
        #
        # Space Complexity:
        # O(1) — Fixed-size arrays of length 26 are used.
        # ---------------------------------------------------------
