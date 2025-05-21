class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        ind = None

        for i in range(len(word) - len(ch) + 1):
            print(word[i:i+len(ch)])
            if word[i:i+len(ch)] == ch:
                ind = i
                break
        
        if ind is None:
            return word
        
        print(ind)

        list1 = list(word)

        list1[:ind+1] = list1[:ind+1][::-1]

        return ''.join(list1)

        