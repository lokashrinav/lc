class TreeNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.dummy = TreeNode()
        self.isEnd = False
        
    def addWord(self, word: str) -> None:
        node = self.dummy
        for i in range(len(word)):
            if word[i] not in node.children.keys():
                node.children[word[i]] = TreeNode()
            node = node.children[word[i]]
            if i == len(word) - 1:
                node.isEnd = True

    def search2(self, start, node, word):
        for i in range(start, len(word)):
            if word[i] == ".":
                for child in node.children.keys():
                    if self.search2(i + 1, node.children[child], word) == True:
                        return True
                return False
            else:
                if word[i] not in node.children.keys():
                    return False
                node = node.children[word[i]]
                if len(word) - 1 == i:
                    return node.isEnd
        return node.isEnd

    def search(self, word: str) -> bool:
        return self.search2(0, self.dummy, word)                
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)