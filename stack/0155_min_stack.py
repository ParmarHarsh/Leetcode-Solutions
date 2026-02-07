class MinStack:
    """
    Stack data structure that supports retrieving the minimum element
    in constant time.

    In addition to the main stack, an auxiliary stack is maintained
    to keep track of the minimum value at each level of the stack.
    """

    def __init__(self):
        """
        Initializes the MinStack with two empty stacks:
        - stack: stores all pushed values
        - min_stack: stores the minimum value corresponding to each state
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Pushes a value onto the stack.

        The value is added to the main stack, and the current minimum
        (either the new value or the previous minimum) is added to
        the min_stack.

        :param val: Integer value to push onto the stack
        """
        self.stack.append(val)

        # If min_stack is empty, the pushed value is the minimum
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # Store the minimum between the new value and the current minimum
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        """
        Removes the top element from the stack.

        Both the main stack and the min_stack are popped to keep
        them in sync.
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """
        Returns the top element of the stack without removing it.

        :return: Top value of the stack
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack in constant time.

        :return: Minimum value currently in the stack
        """
        return self.min_stack[-1]

    # ---------------------------------------------------------
    # Time Complexity:
    # push: O(1)
    # pop: O(1)
    # top: O(1)
    # getMin: O(1)
    #
    # Space Complexity:
    # O(n) — Two stacks are maintained, each storing up to n elements.
    # ---------------------------------------------------------


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
