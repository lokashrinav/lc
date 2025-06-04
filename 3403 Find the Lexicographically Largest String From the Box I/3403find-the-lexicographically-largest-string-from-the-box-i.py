class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word

        def func(str1, str2):

            p1 = p2 = 0

            while p1 < len(str1) or p2 < len(str2):
                if p1 == len(str1):
                    return str2
                elif p2 == len(str2):
                    return str1
                
                if str1[p1] < str2[p2]:
                    return str2
                elif str1[p1] > str2[p2]:
                    return str1
                else:
                    p1 += 1
                    p2 += 1
            
            return str1
        
        biggest = None
        curr = []

        for i in range(len(word)):
            if len(curr) == len(word) - numFriends + 1:
                biggest = curr.copy()
                curr = []
            if biggest is None:
                if not curr or word[i] > curr[0]:
                    curr = []
                curr.append(word[i])
            else:
                if not curr or word[i] > curr[0]:
                    curr = []                    
                if word[i] > biggest[len(curr)]:
                    biggest = None
                    curr.append(word[i])
                else:
                    curr = []

            print(curr, biggest)
        
        return func(''.join(curr), ''.join(biggest)) if biggest is not None else ''.join(curr)
        
        
            