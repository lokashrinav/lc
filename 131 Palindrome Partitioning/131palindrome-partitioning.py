class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final = []
        curr = []
        def back(i):
            print(curr, i)
            if i >= len(s):
                if curr[-1] == curr[-1][::-1]:
                    final.append(curr.copy())
                return
            if not curr:
                curr.append(s[i])
                back(i + 1)
            else:
                curr[-1] += s[i]
                back(i + 1)
                curr[-1] = curr[-1][:-1]
                if curr[-1] == curr[-1][::-1]:
                    curr.append(s[i])
                    back(i + 1)
                    curr.pop()
        back(0)
        
        return final
        