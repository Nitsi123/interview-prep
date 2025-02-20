class TrieNode:
    def __init__(self):
        """Initialize a TrieNode with a dictionary of children and an endOfWord flag."""
        self.children = {}  # Dictionary to store child nodes.
        self.endOfWord = False  # Marks the end of a valid word.

class Trie:
    def __init__(self):
        """Initialize the Trie with a root TrieNode."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()  # Create a new TrieNode if character is not present.
            curr = curr.children[char]  # Move to the next node.
        curr.endOfWord = True  # Mark the end of a word.

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie, otherwise False."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False  # If a character is missing, the word does not exist.
            curr = curr.children[char]  # Move to the next node.
        return curr.endOfWord  # Check if we are at the end of a valid word.

    def startsWith(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False  # If a character is missing, the prefix does not exist.
            curr = curr.children[char]  # Move to the next node.
        return True  # If we reach here, the prefix exists in the Trie.
