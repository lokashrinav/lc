class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        count = 0
        for sentence in sentences:
            words = sentence.split(" ")
            count = max(len(words), count)
        
        return count
        