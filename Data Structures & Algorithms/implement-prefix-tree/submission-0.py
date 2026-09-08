class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        # Mark the final node as a complete word.
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)

        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, text: str):
        node = self.root

        for char in text:
            if char not in node.children:
                return None

            node = node.children[char]

        return node