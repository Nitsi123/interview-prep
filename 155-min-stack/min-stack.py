class MinStack:
    def __init__(self):
        """Initialize two stacks: one for normal values (`stack`) and one for tracking minimums (`minStack`)."""
        self.stack = []  # Stores all values.
        self.minStack = []  # Stores the minimum value at each step.

    def push(self, val: int) -> None:
        """Pushes a value onto the stack while maintaining the minimum value."""
        self.stack.append(val)
        # Push the new minimum value onto minStack (either `val` or the last min).
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        """Removes the top element from the stack while keeping track of the minimum value."""
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        """Returns the top element of the stack."""
        return self.stack[-1]

    def getMin(self) -> int:
        """Returns the minimum element in the stack in O(1) time."""
        return self.minStack[-1]
