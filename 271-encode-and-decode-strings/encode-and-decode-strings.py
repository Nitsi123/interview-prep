from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        
        # Follow-up Questions:
        # 1. Can the strings contain special characters? (Yes, assume any ASCII characters.)
        # 2. Can the strings be empty? (Yes, handle empty strings.)
        # 3. How do we handle special characters like `#`? (Use length-prefix encoding to avoid conflicts.)
        # 4. Can we assume the encoded string fits in memory? (Yes, assume practical constraints.)

        # Brute Force Approach:
        # - Join the strings using a special delimiter.
        # - This can fail if the delimiter appears within a string.
        # - Time Complexity: O(n), where `n` is the total length of all strings.
        # - Space Complexity: O(n), as we store the encoded string.

        # Optimized Approach (Length-Prefix Encoding):
        # - Store the length of each string, followed by a delimiter `#` and the string itself.
        # - This ensures `#` is never ambiguous.
        # - **Encoding Example:**
        #   - Input: `["hello", "world"]`
        #   - Encoded: `"5#hello5#world"`
        # - **Decoding Example:**
        #   - Read until `#` to extract the length.
        #   - Extract the substring using this length.
        # - Time Complexity: O(n), since we process each character once.
        # - Space Complexity: O(n), storing the encoded string.

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s  # Store length before string.
        
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        
        res = []  # List to store decoded strings.
        i = 0  # Pointer for reading the encoded string.

        while i < len(s):
            j = i
            while s[j] != "#":  # Find the delimiter (`#`).
                j += 1
            
            length = int(s[i:j])  # Extract length of the string.
            res.append(s[j + 1: j + 1 + length])  # Extract the actual string.
            i = j + 1 + length  # Move pointer to next encoded string.
        
        return res


# Usage Example:
# codec = Codec()
# encoded = codec.encode(["hello", "world"])
# decoded = codec.decode(encoded)
# print(encoded)  # Output: "5#hello5#world"
# print(decoded)  # Output: ["hello", "world"]
