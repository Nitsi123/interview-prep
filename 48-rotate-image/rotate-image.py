from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Follow-up Questions:
        # 1. What should we do if the input matrix is empty? (Do nothing.)
        # 2. Is the matrix guaranteed to be square? (Yes, assume it's always n x n.)
        # 3. Should the rotation be in-place? (Yes, modify the matrix directly.)
        # 4. Can the matrix contain negative values? (Yes, handle them as valid inputs.)

        # Brute Force Approach:
        # - Create a new matrix of the same size as the input matrix.
        # - For each cell in the input matrix at position (i, j):
        #   - Place its value in the new matrix at position (j, n - i - 1).
        # - Copy the values from the new matrix back to the original matrix.
        # - Time Complexity: O(n^2), where `n` is the number of rows/columns.
        # - Space Complexity: O(n^2), as a new matrix is used.

        # Optimized Approach:
        # - Use a layer-by-layer approach to rotate the matrix in-place:
        #   - For each layer (outer to inner), rotate the four edges of the layer.
        #   - Swap the values between the top, left, bottom, and right edges of the layer.
        # - Time Complexity: O(n^2), as each cell is visited once.
        # - Space Complexity: O(1), as the rotation is done in-place.

        l = 0  # Left pointer for the current layer.
        r = len(matrix) - 1  # Right pointer for the current layer.

        # Iterate over the layers of the matrix.
        while l < r:
            for i in range(r - l):  # Traverse each element in the current layer.
                # Define the top and bottom rows for the current layer.
                top, bottom = l, r

                # Save the value at the top-left position.
                topleft = matrix[top][l + i]

                # Move the bottom-left value to the top-left.
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move the bottom-right value to the bottom-left.
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move the top-right value to the bottom-right.
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move the saved top-left value to the top-right.
                matrix[top + i][r] = topleft

            # Move to the next inner layer.
            l += 1
            r -= 1

        # The matrix is modified in-place, so no return is needed.
