from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Follow-up Questions:
        # 1. Can two cars have the same position? (No, positions are unique.)
        # 2. What if all cars are already at the target? (Return 0 fleets.)
        # 3. What if there is only one car? (Return 1 fleet.)
        # 4. Can speeds be negative? (No, assume all speeds are positive.)

        # Brute Force Approach:
        # - Simulate every car moving towards the target.
        # - Track how fleets merge over time.
        # - Time Complexity: O(n^2), due to checking each car against others.
        # - Space Complexity: O(n), storing fleet information.

        # Optimized Approach (Sorting + Stack Simulation):
        # - **Sort cars by starting position in descending order**.
        # - Compute each car's **time to reach the target**.
        # - Use a **stack** to track fleets:
        #   - If a car's time is greater than the car in front, it forms a new fleet.
        #   - Otherwise, it merges into an existing fleet.
        # - Time Complexity: O(n log n), due to sorting.
        # - Space Complexity: O(n), due to the stack.

        # Step 1: Sort cars based on starting position (descending).
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        current_time = 0  # Tracks the time required for the last fleet to reach the target.

        # Step 2: Process each car
        for pos, spd in cars:
            time_to_target = (target - pos) / spd  # Compute time for car to reach target.

            # If a car takes more time than the current fleet, it starts a new fleet.
            if time_to_target > current_time:
                fleets += 1  # New fleet is formed.
                current_time = time_to_target  # Update the last fleet's time.

        return fleets  # Return total number of fleets.
