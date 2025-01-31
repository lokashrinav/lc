class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        balance, final = 0, s.count(')')
        new_str = []
        for i in range(len(s)):
            if s[i] == '(':
                if balance < final:
                    new_str.append(s[i])
                    balance += 1
            elif s[i] == ')':
                if balance != 0:
                    new_str.append(s[i])
                    balance -= 1
                final -= 1
            else:
                new_str.append(s[i])

        return ''.join(new_str)

        