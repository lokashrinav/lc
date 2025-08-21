class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.end = 0

class Trie:

    def __init__(self):
        self.head = Node()
        
    def insert(self, word: str) -> None:
        node = self.head
        i = 0
        prev = node

        while i < len(word):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                node.children[word[i]] = Node()
                node = node.children[word[i]]
            node.count += 1
            if i == len(word) - 1:
                node.end += 1
            i += 1        

    def countWordsEqualTo(self, word: str) -> int:
        node = self.head
        i = 0

        while i < len(word):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                return 0
            if i == len(word) - 1:
                return node.end
            i += 1     

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.head
        i = 0
        word = prefix

        while i < len(word):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                return 0
            if i == len(word) - 1:
                return node.count
            i += 1   

    def erase(self, word: str) -> None:
        node = self.head
        i = 0

        while i < len(word):
            node = node.children[word[i]]
            node.count -= 1
            if i == len(word) - 1:
                node.end -= 1
            i += 1   


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)