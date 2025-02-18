from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Follow-up Questions:
        # 1. Can `tokens` contain negative numbers? (Yes, assume valid input.)
        # 2. Can division result in decimals? (Yes, but result should be integer truncation.)
        # 3. What if `tokens` is empty? (Invalid input; assume at least one element exists.)
        # 4. Can we assume `tokens` always represent a valid RPN expression? (Yes, assume valid input.)

        # Brute Force Approach:
        # - Convert the expression to infix notation and evaluate it.
        # - This requires parsing the whole expression and handling operator precedence.
        # - Time Complexity: O(n), but more complicated due to parsing.
        # - Space Complexity: O(n), due to extra data structures.

        # Optimized Approach (Using a Stack for Direct Evaluation):
        # - Use a stack to evaluate the RPN expression:
        #   - Push numbers onto the stack.
        #   - When encountering an operator, pop two values, apply the operator, and push the result.
        # - Division should be handled carefully to ensure integer truncation.
        # - Time Complexity: O(n), since we process each token once.
        # - Space Complexity: O(n), for storing numbers in the stack.

        stack = []  # Stack to store operands.

        for c in tokens:
            if c == "+":  # Addition operation.
                stack.append(stack.pop() + stack.pop())
            elif c == "-":  # Subtraction (order matters, so store popped values).
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":  # Multiplication operation.
                stack.append(stack.pop() * stack.pop())
            elif c == "/":  # Division (order matters).
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))  # Integer division with truncation.
            else:  # If it's a number, push it onto the stack.
                stack.append(int(c))

        return stack[0]  # The final result is the last element in the stack.
