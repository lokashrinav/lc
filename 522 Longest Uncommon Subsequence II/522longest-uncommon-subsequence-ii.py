class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        '''

        aba

        '''

        hmap = Counter(strs)


        '''
        50 * 50 * 10 
        '''

        def sub(str1, str2):
            p = 0
            print(str1, str2)
            for i in range(len(str2)):
                if str1[p] == str2[i]:
                    p += 1
                if p == len(str1):
                    print("TRUE")
                    return True
            print("FALSE")
            return False

        saved = 0
        for i in range(len(strs)):
            flag = False
            for p in range(len(strs)):
                if i == p:
                    continue
                if sub(strs[i], strs[p]):
                    flag = True
            if not flag:
                saved = max(saved, len(strs[i]))
        
        return saved if saved else -1

