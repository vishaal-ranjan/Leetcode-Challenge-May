class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(Trie)
        self.is_word_end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            self.is_word_end = True
        else:
            self.children[word[0]].insert(word[1:])
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return self.is_word_end
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)