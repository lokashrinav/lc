class Tree:
    def __init__(self, val, isEnd):
        self.isEnd = isEnd
        self.val = val
        self.children = {}

class Trie:

    def __init__(self):
        self.head = Tree("", False)
        
    def insert(self, word: str) -> None:
        node = self.head
        for i in range(len(word)):
            if word[i] in node.children.keys():
                if i == len(word) - 1:
                    node.children[word[i]].isEnd = True
                else:
                    node = node.children[word[i]]
            else:
                if i == len(word) - 1:
                    node.children[word[i]] = Tree(word[i], True)
                else:
                    node.children[word[i]] = Tree(word[i], False)
                    node = node.children[word[i]]
        
            
    '''def insert(self, word: str) -> None:
        node = self.head
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = Tree(word[i], False)
            node = node.children[word[i]]
            if i == len(word) - 1:
                node.isEnd = True   '''

    def search(self, word: str) -> bool:
        node = self.head
        for i in range(len(word)):
            if i == len(word) - 1 and word[i] in node.children.keys():
                node = node.children[word[i]]
                return node.isEnd
            elif word[i] in node.children.keys():
                node = node.children[word[i]]
            else:
                return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for i in range(len(prefix)):
            if i == len(prefix) - 1 and prefix[i] in node.children.keys():
                return True
            elif prefix[i] in node.children.keys():
                node = node.children[prefix[i]]
            else:
                return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)