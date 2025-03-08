class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.hmap2 = defaultdict(dict)

        for elem in dictionary:
            if elem[0] + elem[-1] not in self.hmap2[len(elem)]:
                self.hmap2[len(elem)][elem[0] + elem[-1]] = set()
            self.hmap2[len(elem)][elem[0] + elem[-1]].add(elem)
                
    def isUnique(self, word: str) -> bool:
        if (word[0] + word[-1]) not in self.hmap2[len(word)]:
            return True
        
        first = next(iter(self.hmap2[len(word)][word[0] + word[-1]]))

        return len(self.hmap2[len(word)][word[0] + word[-1]]) == 1 and first == word

        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)