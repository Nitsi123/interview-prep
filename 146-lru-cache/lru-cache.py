class Node:
    def __init__(self, key, val):
        self.key = key  # The key of the node
        self.val = val  # The value of the node
        self.prev = None  # Pointer to the previous node in the doubly linked list
        self.next = None  # Pointer to the next node in the doubly linked list


class LRUCache:
    def __init__(self, capacity: int):
        # Follow-up Questions:
        # 1. What should happen if we attempt to put a key that already exists? (Update its value.)
        # 2. What happens if capacity is set to 0? (Assume it won't happen, as it's invalid.)
        # 3. Should `get()` operations affect the LRU order? (Yes, move the accessed key to the most recently used position.)

        # Brute Force Approach:
        # - Use a list to store keys and values.
        # - On each `get` or `put`, search for the key in the list:
        #     - If found, move it to the end of the list to simulate LRU order.
        #     - If not found and the list exceeds capacity, remove the first element.
        # - Time Complexity: O(n) per operation due to the need to search for keys.
        # - Space Complexity: O(n) for storing keys and values.

        # Optimized Approach:
        # - Use a hash map (dictionary) for O(1) key lookups.
        # - Use a doubly linked list to maintain LRU order:
        #     - Move recently accessed nodes to the end of the list.
        #     - Remove the least recently used node from the beginning of the list.
        # - Time Complexity: O(1) for both `get` and `put` operations.
        # - Space Complexity: O(n) to store the hash map and doubly linked list.

        self.cap = capacity  # Maximum capacity of the cache
        self.cache = {}  # Hash map to store key-node pairs
        # Create dummy head and tail nodes for the doubly linked list
        self.left = Node(0, 0)  # Dummy head
        self.right = Node(0, 0)  # Dummy tail
        self.left.next = self.right  # Connect head to tail
        self.right.prev = self.left  # Connect tail to head

    def remove(self, node):
        # Removes a node from the doubly linked list
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Inserts a node at the end of the doubly linked list (most recently used position)
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        # Retrieves the value of the given key if it exists in the cache
        if key in self.cache:
            # Move the accessed node to the most recently used position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val  # Return the value of the node
        return -1  # Return -1 if the key is not found

    def put(self, key: int, value: int) -> None:
        # Inserts or updates the value of the given key in the cache
        if key in self.cache:
            # Remove the existing node if the key already exists
            self.remove(self.cache[key])
        # Create a new node and insert it into the cache and linked list
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:  # Check if the cache exceeds its capacity
            # Remove the least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]  # Remove the node from the hash map
