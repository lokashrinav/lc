class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        

        num = ""
        hset = set()

        for i in range(len(word)):
            if word[i].isdigit():
                num += word[i]
            else:
                if num:
                    hset.add(int(num))
                    num = ""

        if num:
            hset.add(int(num))

        return len(hset)