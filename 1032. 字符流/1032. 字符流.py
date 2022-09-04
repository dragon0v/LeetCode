from typing import *
class StreamChecker:
    # 纯纯的从trie来的摆烂
    def __init__(self, words: List[str]):
        self.crtwords = []
        self.j = 0
        self.t = Trie()
        for word in words:
            self.t.insert(word)

    def query(self, letter: str) -> bool:
        for i in range(len(self.crtwords)):
            self.crtwords[i] = self.crtwords[i]+letter
        self.crtwords.append(letter)

        temp = []  # 这里可以优化内存，全在crtwords做就可以了
        flag = False
        for w in self.crtwords:
            s = self.t.startsWith(w)
            if s==1:
                temp.append(w)
            elif s==2:
                temp.append(w)
                flag = True
        
        self.crtwords = temp
        if flag:
            return True
        return False




# LC208
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
        node = self
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

    def startsWith(self, prefix: str):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            o = ord(c)-ord('a')
            if node.children[o] == None:
                return -1
            else:
                node = node.children[o]
        if node.isEnd:
            return 2
        else:
            return 1

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)