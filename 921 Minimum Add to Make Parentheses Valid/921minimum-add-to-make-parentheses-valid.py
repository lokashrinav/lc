class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance, final = 0, s.count(")")
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            else:
                if balance == 0:
                    count += 1
                else:
                    balance -= 1
        
        return count + balance
        