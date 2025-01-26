from typing import List

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Follow-up Questions:
        # 1. What should we return if there are fewer than k factors? (Return -1.)
        # 2. Can n be 1? (Yes, handle it as a special case where the only factor is 1.)
        # 3. Are the factors guaranteed to be unique? (Yes, factors of a number are always unique.)
        # 4. What is the maximum possible value of n? (Assume it fits within standard integer limits.)

        # Optimized Approach:
        # - Iterate through all integers from 1 to sqrt(n) to find factors:
        #   - If `i` divides `n`, it is a factor.
        #   - Store the smaller factor `i` in one list (`small_facts`) and the corresponding larger factor `n // i` in another list (`large_facts`).
        #   - Avoid duplication by ensuring `i != n // i`.
        # - Combine the two lists (`small_facts` and the reverse of `large_facts`) to get all factors in sorted order.
        # - Return the k-th factor from the combined list, or -1 if k exceeds the number of factors.
        # - Time Complexity: O(sqrt(n)), as we only iterate up to sqrt(n).
        # - Space Complexity: O(sqrt(n)), for storing the factors.

        small_facts = []  # List to store smaller factors of n.
        large_facts = []  # List to store larger factors of n.

        # Step 1: Iterate through integers from 1 to sqrt(n).
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:  # If `i` is a factor of `n`:
                small_facts.append(i)  # Add the smaller factor.
                
                # If the corresponding larger factor is different, add it to `large_facts`.
                if i != n // i:
                    large_facts.append(n // i)
        
        # Step 2: Combine the smaller factors and the reverse of the larger factors.
        res = small_facts + large_facts[::-1]

        # Step 3: Return the k-th factor if it exists, or -1 if k exceeds the number of factors.
        return res[k-1] if k <= len(res) else -1
