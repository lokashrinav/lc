class MagicDictionary:

    def __init__(self):
        self.hmap = defaultdict(list)
        self.dict = None
        
    def buildDict(self, dictionary: List[str]) -> None:
        for i in range(len(dictionary)):
            for p in range(len(dictionary[i])):
                new_str =  dictionary[i][:p] + "*" + dictionary[i][p+1:]
                self.hmap[new_str].append(dictionary[i])
        
    def search(self, searchWord: str) -> bool:
        for p in range(len(searchWord)):
            new_str = searchWord[:p] + "*" + searchWord[p+1:]
            if new_str in self.hmap and (searchWord not in self.hmap[new_str] or len(self.hmap[new_str]) > 1):
                return True
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)