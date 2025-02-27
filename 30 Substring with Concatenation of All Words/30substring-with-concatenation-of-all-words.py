class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # n^2

        '''
        barfoothefoobarman
        011011111011011111
        '''
        word_length = len(words[0])
        word_count = len(words)

        hmap = defaultdict(int)
        for word in words:
            hmap[word] += 1

        def check(word):
            hmap2 = defaultdict(int)
            for i in range(0, len(word), word_length):
                hmap2[word[i:i+word_length]] += 1

            return hmap2 == hmap

        final = []
        for i in range(len(s) - word_length*word_count + 1):
            #print(s[i:i+word_length * word_count])
            if check(s[i:i+word_length * word_count]):
                final.append(i)
        
        return final



        