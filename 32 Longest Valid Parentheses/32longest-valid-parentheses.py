class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        def check(s):
            l, r = 0, 0
            count = 0
            maxLen = 0
            while r < len(s):
                changed = False
                if s[r] == ")" and count == 0:
                    changed = True
                elif s[r] == "(":
                    count += 1
                    r += 1
                elif s[r] == ")":
                    count -= 1
                    r += 1
                if count == 0:
                    maxLen = max(maxLen, r - l)
                if changed:
                    l = r + 1
                    r = l
                    count = 0
            return maxLen
        
        def check2(s):
            l, r = len(s) - 1, len(s) - 1
            count = 0
            maxLen = 0
            while l >= 0:
                changed = False
                if s[l] == "(" and count == 0:
                    changed = True
                elif s[l] == ")":
                    count += 1
                    l -= 1
                elif s[l] == "(":
                    count -= 1
                    l -= 1
                if count == 0:
                    maxLen = max(maxLen, abs(r - l))
                if changed:
                    r = l - 1
                    l = r
                    count = 0
                print(count, maxLen)
            return maxLen
        
        return max(check(s), check2(s))


            