class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isEnd = False # 表示有到这结束的单词


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self # TODO 啥意思
        for c in word:
            o = ord(c)-ord('a')
            if node.children[o] == None:
                node.children[o] = Trie()
            node = node.children[o]
        node.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for c in word:
            o = ord(c)-ord('a')
            if node.children[o] == None:
                return False
            else:
                node = node.children[o]
        if node.isEnd == True:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            o = ord(c)-ord('a')
            if node.children[o] == None:
                return False
            else:
                node = node.children[o]
        return True

# 看了题解的

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)