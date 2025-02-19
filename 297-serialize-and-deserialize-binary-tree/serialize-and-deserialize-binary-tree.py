class Codec:
    # Follow-up Questions:
    # 1. Can the tree contain negative values? (Yes, assume all integers are valid.)
    # 2. Should we preserve the exact structure? (Yes, must be identical after deserialization.)
    # 3. Can the tree be unbalanced? (Yes, works for any shape.)
    # 4. How should we handle an empty tree? (Return `""` for serialization, `None` for deserialization.)

    # Brute Force Approach:
    # - Use **level-order traversal** and store `None` for missing children.
    # - Use a queue for BFS, adding left and right nodes iteratively.
    # - Time Complexity: O(n), as each node is visited once.
    # - Space Complexity: O(n), since we store all nodes.

    # Optimized Approach (Preorder DFS with Null Markers):
    # - Serialize using **preorder traversal (Root → Left → Right)**.
    # - Store `"N"` for null nodes to preserve structure.
    # - Deserialize by **reconstructing using preorder recursion**.
    # - Time Complexity: O(n), since each node is visited once.
    # - Space Complexity: O(n), due to recursion depth.

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []  # Store serialized tree data.

        def dfs(node):
            if not node:
                res.append("N")  # Use 'N' to represent null nodes.
                return
            res.append(str(node.val))  # Store node value.
            dfs(node.left)  # Serialize left subtree.
            dfs(node.right)  # Serialize right subtree.

        dfs(root)  # Start DFS from root.
        return ",".join(res)  # Convert list to comma-separated string.

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")  # Convert serialized string back to list.
        self.i = 0  # Pointer to track current node in `vals`.

        def dfs():
            if vals[self.i] == "N":  # If "N", return None (null node).
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))  # Create node.
            self.i += 1
            node.left = dfs()  # Rebuild left subtree.
            node.right = dfs()  # Rebuild right subtree.
            return node

        return dfs()  # Start deserialization.
