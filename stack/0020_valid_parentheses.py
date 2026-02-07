class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines whether a string of brackets is valid.

        A string is considered valid if:
        - Open brackets are closed by the same type of brackets.
        - Open brackets are closed in the correct order.
        - Every closing bracket has a corresponding opening bracket.

        :param s: Input string containing only brackets
        :return: True if the string is valid, otherwise False
        """

        # Mapping of closing brackets to their corresponding opening brackets
        my_map = {")": "(", "}": "{", "]": "["}

        # List used as a stack to track opening brackets
        my_list = list()

        # Iterate through each character in the string
        for ch in s:
            # If the character is an opening bracket, push it onto the stack
            if ch not in my_map:
                my_list.append(ch)
                continue

            # If the stack is empty or the top does not match the expected opening bracket
            if not my_list or my_map[ch] != my_list[-1]:
                return False

            # Pop the matched opening bracket from the stack
            my_list.pop()

        # If the stack is empty, all brackets were matched correctly
        return not my_list

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each character in the string is processed once.
        #
        # Space Complexity:
        # O(n) — In the worst case, all opening brackets are stored
        #        in the stack.
        # ---------------------------------------------------------
