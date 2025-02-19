class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total = 0  # Current sum of elements in the subset
        subset = []  # Current subset being explored
        res = []  # Result list to hold all valid combinations

        def helper(i, subset, total):
            if total == target:  # If current total equals the target, store the subset
                res.append(subset.copy())
                return
            
            if total > target or i >= len(candidates):  # Exceeding target or out of bounds
                return  # Backtrack
            
            # Include the current number and stay on this index (since we can reuse elements)
            subset.append(candidates[i])
            helper(i, subset, total + candidates[i])

            # Exclude the current number and move to the next index
            subset.pop()
            helper(i + 1, subset, total)
        
        helper(0, subset, total)  # Start recursion
        return res

# Time Complexity: O(2^t) where t is the target sum, as in worst case we explore 2 options per step.
# Space Complexity: O(k) where k is the average depth of the recursion tree which depends on the target and minimum value in candidates.



            

        


        