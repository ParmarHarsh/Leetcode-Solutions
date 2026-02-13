from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates the value of an arithmetic expression in Reverse Polish Notation (RPN).

        The function uses a stack to process operands and operators.
        When an operator is encountered, the top two elements are popped
        from the stack, the operation is performed, and the result is
        pushed back onto the stack.

        :param tokens: List of strings representing the RPN expression
        :return: Integer result of the evaluated expression
        """

        # Stack to store operands during evaluation
        my_stack = []

        # Iterate through each token in the input list
        for token in tokens:
            # If the token is not an operator, convert it to an integer
            # and push it onto the stack
            if token not in "+-/*":
                my_stack.append(int(token))
            else:
                # Pop the top two operands from the stack
                a = my_stack.pop()
                b = my_stack.pop()

                # Perform the corresponding operation
                if token == "+":
                    my_stack.append(a + b)

                if token == "-":
                    my_stack.append(b - a)

                if token == "*":
                    my_stack.append(b * a)

                if token == "/":
                    # Division should truncate toward zero
                    my_stack.append(int(b / a))

        # The final result will be the only element left in the stack
        return my_stack[0]

        # ---------------------------------------------------------
        # Time Complexity:
        # O(n) — Each token is processed exactly once.
        #
        # Space Complexity:
        # O(n) — The stack may store up to n elements in the worst case.
        # ---------------------------------------------------------
