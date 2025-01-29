from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Follow-up Questions:
        # 1. Can the input contain duplicate numbers? (Yes, handle duplicates in the result.)
        # 2. Should the triplets be returned in sorted order? (Yes, each triplet must be in ascending order.)
        # 3. Can the same triplet be included multiple times in the result? (No, remove duplicates.)
        # 4. What is the expected time complexity? (Better than O(n^3), ideally O(n^2).)
        # 5. What should we return if no valid triplets exist? (Return an empty list.)

        # Brute Force Approach:
        # - Generate all possible triplets (i, j, k) where i < j < k.
        # - Check if nums[i] + nums[j] + nums[k] == 0.
        # - Use a set to ensure unique triplets.
        # - Time Complexity: O(n^3), due to three nested loops.
        # - Space Complexity: O(n), for storing results in a set.

        # Optimized Approach (Two-Pointer):
        # - Sort the input array.
        # - Iterate through the array, treating each number as the first number in a triplet.
        # - Use two pointers (`l` and `r`) to find two numbers that sum to the negative of the first number.
        # - Skip duplicate values to avoid duplicate triplets.
        # - Time Complexity: O(n^2), since we iterate and use two pointers.
        # - Space Complexity: O(n), for storing results.

        res = []  # List to store unique triplets.
        nums.sort()  # Sorting ensures we can use the two-pointer approach.

        for i in range(len(nums)):
            # Skip duplicate values for the first element.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1  # Two-pointer initialization.
            target = -nums[i]  # The sum we need to find.

            while l < r:
                three_sum = nums[l] + nums[r]
                
                if three_sum == target:
                    res.append([nums[i], nums[l], nums[r]])

                    # Skip duplicate values for the second element.
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Skip duplicate values for the third element.
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # Move both pointers after adding a valid triplet.
                    l += 1
                    r -= 1
                
                elif three_sum < target:
                    l += 1  # Move left pointer to increase sum.
                else:
                    r -= 1  # Move right pointer to decrease sum.

        return res  # Return the list of unique triplets.
