class Node:
    def __init__(self):
        self.isEnd = False
        self.hmap = {}

class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head
        for i in range(len(word)):
            if word[i] not in curr.hmap:
                curr.hmap[word[i]] = Node()
            curr = curr.hmap[word[i]]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.head
        for i in range(len(word)):
            if word[i] in curr.hmap:
                curr = curr.hmap[word[i]]
            else:
                return False

        return curr.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for i in range(len(prefix)):
            if prefix[i] in curr.hmap:
                curr = curr.hmap[prefix[i]]
            else:
                return False

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)